from google.appengine.ext import ndb


class VsiFilmi:
    def __init__(self,id_s,img,naziv,ocena,datum_izdaje,opis):
        self.id_s = id_s
        self.img = img
        self.naziv = naziv
        self.ocena = ocena
        self.datum_izdaje = datum_izdaje
        self.opis = opis


class PriljubljeniFilmi(ndb.Model):
        film_id = ndb.StringProperty()
        naziv = ndb.StringProperty()
        opis = ndb.StringProperty()
        img = ndb.StringProperty()
        ocena = ndb.StringProperty()
        datum_izdaje = ndb.StringProperty()
