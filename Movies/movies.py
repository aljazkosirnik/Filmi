from models import AllMovies
import json
from urllib.request import urlopen


def get_movies(page):

    vsi = []
    img_path = "https://image.tmdb.org/t/p/w500/"

    # variable "stran" is from url example /stran/1/ , /stran/2/
    url = "https://api.themoviedb.org/3/movie/popular?api_key=26df55ce52689aa1d352444f3918da77&language=en-US&page=" + str(page)
    response_url = urlopen(url)
    data = json.loads(response_url.read().decode("utf-8"))
    result = data["results"]
    for i in result:
        vsi.append(AllMovies(i["id"], img_path + i["poster_path"], i["title"], i["vote_average"], i["release_date"]))
    return vsi


def get_movie_category(category, page):

    vsi = []
    img_path = "https://image.tmdb.org/t/p/w500/"

    # variable "category" is from url example /kategorija/filmi/28/ , /kategorija/filmi/2/
    # variable "stran" is from url example /kategorija/filmi/28/stran/1 , /kategorija/filmi/23/stran/2
    url = "https://api.themoviedb.org/3/discover/movie?api_key=26df55ce52689aa1d352444f3918da77&language=en-US&sort_by=popularity.desc&with_genres=" + str(category) + "&page=" + str(page)
    response_url = urlopen(url)
    data = json.loads(response_url.read().decode("utf-8"))
    result = data["results"]
    for i in result:
        vsi.append(AllMovies(i["id"], img_path + i["poster_path"], i["title"], i["vote_average"], i["release_date"]))
    return vsi
