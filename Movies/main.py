#!/usr/bin/env python
import os
import jinja2
import webapp2
import json
from urllib2 import urlopen
from models import *
import logging
from webob import Request
from google.appengine.api import users

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)

stran = 1
request = Request.blank('/')


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if params is None:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        global stran

        vsi = []
        img_path = "https://image.tmdb.org/t/p/w500/"
        url = "https://api.themoviedb.org/3/movie/popular?api_key=26df55ce52689aa1d352444f3918da77&language=en-US&page=" + str(stran)
        response_url = urlopen(url)
        data = json.loads(response_url.read().decode("utf-8"))
        result = data["results"]
        for i in result:
            vsi.append(VsiFilmi(i["id"], img_path + i["poster_path"], i["title"], i["vote_average"], i["release_date"], i["overview"]))

        params = {
            "vsi": vsi,
            "stran": stran
        }

        return self.render_template("index.html", params=params)

    def post(self):
        global stran
        global film_id
        domov_gumb = self.request.get("domov")
        prejsnji_gumb = self.request.get("prejsna-stran")
        naslednji_gumb = self.request.get("naslednja-stran")
        vec_gumb = self.request.get("vec")
        dodaj_gumb = self.request.get("dodaj")

        if domov_gumb:
            stran = 1
        elif prejsnji_gumb:
            if stran == 1:
                stran = 1
            else:
                stran -= 1
        elif naslednji_gumb:
            stran += 1

        if vec_gumb:
            return self.redirect_to("film")
        elif dodaj_gumb:
            film_id = self.request.get("film_id")
            naziv = self.request.get("naziv")
            opis = self.request.get("opis")
            img = self.request.get("img")
            ocena = self.request.get("ocena")
            datum_izdaje = self.request.get("datum_izdaje")

            filmi = PriljubljeniFilmi(film_id=film_id, naziv=naziv, opis=opis, img=img, ocena=ocena, datum_izdaje=datum_izdaje)
            filmi.put()
            return self.redirect_to("moji-filmi")
        return self.redirect_to("filmi")


class FilmHandler(BaseHandler):
    def get(self, film_id):

        url = "https://api.themoviedb.org/3/movie/" + film_id + "?api_key=26df55ce52689aa1d352444f3918da77&language=en-US"
        response_url = urlopen(url)
        data = json.loads(response_url.read().decode("utf-8"))

        id_s = data["id"]
        slika = "https://image.tmdb.org/t/p/w500/" + data["poster_path"]
        back_slika = "https://image.tmdb.org/t/p/original" + data["backdrop_path"]
        naziv = data["title"]
        ocena = data["vote_average"]
        datum_izdaje = data["release_date"]
        opis = data["overview"]
        kratek_opis = data["tagline"]
        proracun = data["budget"]
        zasluzek = data["revenue"]
        cas = data["runtime"]
        # Spodaj so listi
        zvrsti = []
        produkcija = []
        produkcija_img = []

        zvrsti_list = data["genres"]
        z = 0
        while z < len(zvrsti_list):
            zvrsti.append(zvrsti_list[z]["name"])
            z += 1

        produkcija_list = data["production_companies"]
        p = 0
        while p < len(produkcija_list):
            produkcija.append(produkcija_list[p]["name"])
            produkcija_img.append(produkcija_list[p]["logo_path"])
            p += 1

        # Video ne dela ker je prevec http requestov na enem page-u?   ---   raise HTTPError(req.get_full_url(), code, msg, hdrs, fp) HTTPError: HTTP Error 429: Unknown   ---
        # video_url = "https://api.themoviedb.org/3/movie/" + film_id + "/videos?api_key=26df55ce52689aa1d352444f3918da77&language=en-US"
        # video_response_url = urlopen(video_url)
        # video_data = json.loads(video_response_url.read().decode("utf-8"))
        # video = "https://www.youtube.com/embed/" + video_data["results"][0]["key"]

        params = {"slika": slika, "back_slika": back_slika, "film_id": id_s, "naziv": naziv, "ocena": ocena, "datum_izdaje": datum_izdaje, "opis": opis, "kratek_opis": kratek_opis,
                  "proracun": proracun, "zasluzek": zasluzek, "cas": cas, "zvrsti": zvrsti, "produkcija": produkcija, "produkcija_img": produkcija_img}
        # , "video": video}

        return self.render_template("film.html", params=params)


class MojiFilmiHandler(BaseHandler):
    def get(self):
        moji_filmi = PriljubljeniFilmi.query().fetch()
        params = {
            "moji_filmi": moji_filmi
        }
        return self.render_template("moji-filmi.html", params=params)


class IzbrisiHandler(BaseHandler):
    def get(self, film_id):
        film = PriljubljeniFilmi.get_by_id(int(film_id))
        film.key.delete()
        return self.redirect_to("filmi")

    def post(self, film_id):
        film = PriljubljeniFilmi.get_by_id(int(film_id))
        film.key.delete()
        return self.redirect_to("filmi")


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler, name="filmi"),
    webapp2.Route('/film/<film_id:(\d+)>/', FilmHandler, name="film"),
    webapp2.Route('/moji-filmi/', MojiFilmiHandler, name="moji-filmi"),
    webapp2.Route('/izbrisi/<film_id:\d+>/', IzbrisiHandler),
], debug=True)
