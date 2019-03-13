from models import AllShows
import json
from urllib2 import urlopen


def get_shows(page):

    vsi = []
    img_path = "https://image.tmdb.org/t/p/w500/"

    # variable "stran" is from url example /stran/1/ , /stran/2/
    url = "https://api.themoviedb.org/3/tv/popular?api_key=26df55ce52689aa1d352444f3918da77&language=en-US&page=" + str(page)
    response_url = urlopen(url)
    data = json.loads(response_url.read().decode("utf-8"))
    result = data["results"]
    for i in result:

        if i["poster_path"] is None:
            print str(i["poster_path"]) + "THERE IS NO POSTER PATH"

        else:
            vsi.append(AllShows(i["id"], img_path + i["poster_path"], i["name"], i["vote_average"], i["first_air_date"]))
    return vsi


def get_show_category(category, page):

    vsi = []
    img_path = "https://image.tmdb.org/t/p/w500/"

    # variable "category" is from url example /kategorija/oddaje/10759/ , /kategorija/oddaje/23/
    # variable "stran" is from url example /kategorija/oddaje/10759/stran/2 , /kategorija/oddaje/10759/stran/1
    url = "https://api.themoviedb.org/3/discover/tv?api_key=26df55ce52689aa1d352444f3918da77&language=en-US&sort_by=popularity.desc&with_genres=" + str(category) + "&page=" + str(page)
    response_url = urlopen(url)
    data = json.loads(response_url.read().decode("utf-8"))
    result = data["results"]
    for i in result:

        if i["poster_path"] is None:
            print str(i["poster_path"]) + "THERE IS NO POSTER PATH"

        else:
            vsi.append(AllShows(i["id"], img_path + i["poster_path"], i["name"], i["vote_average"], i["first_air_date"]))
    return vsi
