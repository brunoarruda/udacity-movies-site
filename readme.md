# Movie Site Project

This project is part of the assignments of the Udacity Nanodegree Full-Stack Web Developer. It generates a page of movies according to a list of titles.

# How to use

You must have a valid [Movie DB API](https://developers.themoviedb.org/3/getting-started/introduction) key. Follow the instructions to get one.

1. Download this repo
2. Remove in the config file and the movie list file the "-TEMPLATE" part.
3. Save your key in the entertainment_center.config.
4. Write the titles in movie_list.tx in the form "```movie_title, youtube_trailer_link, yes|no```". Write yes if you have watched, no otherwise. 
5. Run entertainment_center.py. It will create or overwrite a index.html file in the script directory.