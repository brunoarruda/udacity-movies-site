import webbrowser

class Movie(object):
    poster_quality = "w500"
    poster_url = "https://image.tmdb.org/t/p/{}/".format(poster_quality)
    
    def __init__(self, json_data, trailer_url = None, watched = "no"):
        self.title = json_data['title']
        self.poster_image_url = self.poster_url + \
            json_data['poster_path'][1:]
        self.storyline = json_data['overview']
        month, day, year = json_data['release_date'].split('-')
        self.release_date = "{}/{}/{}".format(day, month, year)
        self.trailer_youtube_url = trailer_url
        self.watched = False
        if watched.lower() == "yes":
            self.watched = True


    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
