import fresh_tomatoes
import media


"""The following are instances of the movie class, located in media.py, each
movie object is created by calling the Movie class constructor by calling
media.Movie(title, plot, poster_url, trailer_url). The title and plot where
written from memory while both the poster and trailer url were found online."""

about_alex = media.Movie('About Alex',
                         'College friends reunite after one attempts suicide.',
                         'https://upload.wikimedia.org/wikipedia/en/1/19/About_alex_poster.jpg',
                         'https://www.youtube.com/watch?v=YGraucjOUGI')

bettlejuice = media.Movie('Beetlejuice',
                          'A deceased couple get stuck haunting their home.',
                          'https://upload.wikimedia.org/wikipedia/en/a/ac/Beetlejuice_film_poster.jpg',
                          'https://www.youtube.com/watch?v=2hovKm9oFiM')

dead_poets_society = media.Movie('Dead Poets Society',
                                 'A new English teacher teaches his students more than just English.',
                                 'https://upload.wikimedia.org/wikipedia/en/4/49/Dead_poets_society.jpg',
                                 'https://www.youtube.com/watch?v=4lj185DaZ_o')

la_la_land = media.Movie('La La Land',
                         'A couple in LA trying to achieve their dreams while staying love.',
                         'https://upload.wikimedia.org/wikipedia/en/a/ab/La_La_Land_%28film%29.png',
                         'https://www.youtube.com/watch?v=0pdqf4P9MB8')

one_day = media.Movie('One Day',
                      'Two friends and their unrequited love.',
                      'https://upload.wikimedia.org/wikipedia/en/a/ad/One_Day_Poster.jpg',
                      'https://www.youtube.com/watch?v=zVuuooZqVaU')

tron = media.Movie('Tron Legacy',
                   'A boy tries to save his father from a cyber world.',
                   'https://upload.wikimedia.org/wikipedia/en/c/c2/Tron_Legacy_poster.jpg',
                   'https://www.youtube.com/watch?v=L9szn1QQfas')

movies = [about_alex, bettlejuice, dead_poets_society, la_la_land, one_day, tron]
fresh_tomatoes.open_movies_page(movies)
