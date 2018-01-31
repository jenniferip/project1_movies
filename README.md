# Jennifer's Movies

Jennifer's movies is a folder containing the files used to create a webpage listing my favorite movies. The page is a list of movie posters with the name of the movie under them and when you click on any movie poster, the movie's trailer is shown. 

## How to run 

Assuming you have the folder downloaded containing the necessary files. From terminal, you want to be in the jennifers_movie folder then you run the following code:
 ```python entertainment_center.py``` 

## Files

The files included are: 
* media.py - This file defines the Movie class. It contains the movie object constructor to store movie instance variables including the movie's title, plot, poster and trailer urls and it defines the instance methods: `show_trailer()` and `show_poster()`.
* entertainment_center.py - This files creates all the movie object instances relating to my favorite movies, puts them in a list which is then called as the variable for the `open_movie_page()` function from the fresh_tomatoes.py file.
* fresh_tomatoes.py - This file holds the HTML formulation that actually creates the movie website and its layout. 
* fresh_tomatoes.html - This is the HTML website file created from fresh_tomatoes.py