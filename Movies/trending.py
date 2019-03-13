from models import Trending
import json
from urllib.request import urlopen


def get_trending():

    # Get data
    trending = []
    img_path = "https://image.tmdb.org/t/p/w500/"
    trending_url = "https://api.themoviedb.org/3/trending/all/day?api_key=26df55ce52689aa1d352444f3918da77"
    trending_response_url = urlopen(trending_url)
    trending_data = json.loads(trending_response_url.read().decode("utf-8"))
    trending_result = trending_data["results"]

    for x in trending_result:
        url = ""

        # Since movie has key named "title" and TV show has key named "name" it needs to be checked which one is it
        if "title" in x:
            title = x["title"]
            url = "film"
        else:
            title = x["name"]
            url = "oddaja"

        # Since movie has key named "release_date" and TV show has key named "first_air_date" it needs to be checked which one is it
        if "release_date" in x:
            release_date = x["release_date"]
        else:
            release_date = x["first_air_date"]

        trending.append(Trending(x["id"], img_path + x["poster_path"], title, x["vote_average"], release_date, url))

    return trending
