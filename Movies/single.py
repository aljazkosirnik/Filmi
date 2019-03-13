import json
from urllib2 import urlopen


# Get single movie will be called when user goes on /film/single_id URL
def get_single_movie(single_id):
    url = "https://api.themoviedb.org/3/movie/" + single_id + "?api_key=26df55ce52689aa1d352444f3918da77&language=en-US"
    response_url = urlopen(url)
    data = json.loads(response_url.read().decode("utf-8"))

    img = "https://image.tmdb.org/t/p/w500/" + data["poster_path"]
    back_img = "https://image.tmdb.org/t/p/original" + data["backdrop_path"]

    genres = []
    genres_id = []
    production = []
    production_img = []

    genres_list = data["genres"]

    production_list = data["production_companies"]
    p = 0
    while p < len(production_list):
        production.append(production_list[p]["name"])
        production_img.append(production_list[p]["logo_path"])
        p += 1

    video_url = "https://api.themoviedb.org/3/movie/" + single_id + "/videos?api_key=26df55ce52689aa1d352444f3918da77&language=en-US"
    video_response_url = urlopen(video_url)
    video_data = json.loads(video_response_url.read().decode("utf-8"))
    video = "https://www.youtube.com/embed/" + video_data["results"][0]["key"]

    # Pass trough the page all that I get with the API
    params = {"img": img, "back_img": back_img, "single_id": data["id"], "title": data["title"], "vote_average": data["vote_average"], "release_date": data["release_date"],
              "overview": data["overview"], "tagline": data["tagline"], "budget": data["budget"], "revenue": data["revenue"], "runtime": data["runtime"], "genres": genres_list,
              "production": production, "production_img": production_img, "video": video}

    return params


# Get single show will be called when user goes on /oddaja/single_id URL
def get_single_show(single_id):
    url = "https://api.themoviedb.org/3/tv/" + single_id + "?api_key=26df55ce52689aa1d352444f3918da77&language=en-US"
    response_url = urlopen(url)
    data = json.loads(response_url.read().decode("utf-8"))

    img = "https://image.tmdb.org/t/p/w500/" + data["poster_path"]
    back_img = "https://image.tmdb.org/t/p/original" + data["backdrop_path"]

    genres = []

    genres_list = data["genres"]
    z = 0
    while z < len(genres_list):
        genres.append(genres_list[z]["name"])
        z += 1

    video_url = "https://api.themoviedb.org/3/tv/" + single_id + "/videos?api_key=26df55ce52689aa1d352444f3918da77&language=en-US"
    video_response_url = urlopen(video_url)
    video_data = json.loads(video_response_url.read().decode("utf-8"))
    video = "https://www.youtube.com/embed/" + video_data["results"][0]["key"]

    # Pass trough the page all that I get with the API
    params = {"img": img, "back_img": back_img, "single_id": data["id"], "title": data["name"], "vote_average": data["vote_average"], "release_date": data["first_air_date"],
              "overview": data["overview"], "genres": genres, "video": video, "season": data["seasons"], "number_of_seasons": data["number_of_seasons"], "number_of_episodes": data["number_of_episodes"]}

    return params
