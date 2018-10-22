#!/usr/bin/env python3

import json
import re
import urllib.request
import urllib.parse

import fresh_tomatoes
import media

# Global constants

FILENAME = {
    'config': "entertainment_center.config",
    'movies_list': 'movie_list.txt'
}

THEMOVIEDB_URL = "https://api.themoviedb.org/3/search/movie?"

THEMOVIEDB_API_CONFIG = {
    'api_key': None,
    'language': "pt-BR",
    'query': None
}


def configure():
    """Loads the API key of The Movie DB from a file as defined in FILENAME

    Raises:
        RuntimeError:
            The specified file doesn't contain a line starting with "api_key".
    """
    global THEMOVIEDB_API_CONFIG
    with open(FILENAME['config'], "r") as config_file:
        key_line = [x for x in config_file.readlines()
                    if x.startswith('api_key')]
        if key_line:
            key = key_line[0].split("=")[1]
            # removes residual characters from the key
            key = re.sub("\r|\n| ", "", key)
            THEMOVIEDB_API_CONFIG['api_key'] = key
        else:
            msg = ('O arquivo {} não contém uma linha com '
                   'formato "api_key=sua chave"')
            raise RuntimeError(msg.format(FILENAME['config']))


def get_movies():
    """Queries The Movie DB API for each movie in the movies list file.

    Returns:
        A list with media.Movie objects related to the queries performed.
    """
    global THEMOVIEDB_API_CONFIG
    movies = []
    with open(FILENAME['movies_list'], "r", encoding="utf-8") as movie_file:
        movie_data = [x for x in movie_file.readlines() if x != ""]
        for line in movie_data:
            title, trailer_url, watched = line.split(",")
            THEMOVIEDB_API_CONFIG['query'] = title.rstrip()
            movie_data = query_external_api()
            movie = media.Movie(movie_data,
                                trailer_url.rstrip(),
                                re.sub("\r|\n| ", "", watched))
            movies.append(movie)
    return movies


def query_external_api():
    url = THEMOVIEDB_URL + urllib.parse.urlencode(THEMOVIEDB_API_CONFIG)
    with urllib.request.urlopen(url) as connection:
        data = json.load(connection)
        return data['results'][0]


def main():
    configure()
    fresh_tomatoes.open_movies_page(get_movies())


if __name__ == '__main__':
    main()
