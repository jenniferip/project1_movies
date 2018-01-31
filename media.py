import webbrowser


class Movie():
    """This class creates space to store movie objects defined by their title,
    plot, movie poster url, and youtube trailer url."""

    VALID_RATINGS = ['G', 'PG', 'PG-13', 'R']

    def __init__(self, movie_title, movie_storyline,
                 movie_poster, movie_trailer):
        """Constructor for the Movie class. Creates space to store movie objects
        and their information including the movie's title, storyline,
        movie poster url, and movie trailer url."""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_trailer

    def show_trailer(self):
        """Use to show a movie's trailer by using the open function in
        the webbbrowser module to open the trailer_youtube_url variable
        associated which the particular movie instance."""
        webbrowser.open(self.trailer_youtube_url)

    def show_poster(self):
        """Use to show a movie's poster by again using the open function
        from the webbrowser module to open the movie poster url associated
        with the trailer_youtube_url variable for the particular movie
        instance."""
        webbrowser.open(self.poster_image_url)
