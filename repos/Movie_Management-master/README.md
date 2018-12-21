#Project Title-Movie Management System.
This project is created to deals with movie management.It is created in python using Django Framework and tested
On PostgreSQL Database.

##Prereqiusite:

    -Python 2.7
    -Django 1.8
    -Postman
    -PostgreSQL Database
    
##Functionalities:

    User can add new movies by using POSTMAN.
    User can Get movies By Genre.
    User can search movie and partial search by keywords.
    User can get Artist/Actor Statistics which include Movies,Average Ratings,Best Movie On the basis of movie ratings.
    User can search movies By Director Name.
    User can search movies by Year. Assumption(searching by month will no provide enough information).
    
##API’s Implemented:

    -GET /genre/<genre>  http://127.0.0.1:8000/movie/genre/<genre>
    -GET /search/<partial_name>  http://127.0.0.1:8000/movie/search/<keyword>
    -POST /add_new_movie/.  http://127.0.0.1:8000/movie/newmovie
    -GET /director/<director>.  http://127.0.0.1:8000/movie/director/<director>
    -GET /star/ should return stats like total movies, average rating, most http://127.0.0.1:8000/movie/star/<artist name>successful movie.
    -GET /year/<year>. http://127.0.0.1:8000/movie/year/<year>

##Running the Project:

    To run the code just open terminal and go to the directory where the code folder is there . 
    Run server by using command [python manage.py runserver]
    There are certain urls provided to run certain urls as mentioned above.
    For PostgreSQL use port 5434

 







