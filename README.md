# final_hands-on_exam
Final hands-on exam for IT6
by Magno, Gideon T.

******************************************************************************************
This is my final hands-on project for the subject IT6.
In this project, we can preview, add, and manipulate the database 'songlist' using python.
******************************************************************************************
Requirements:
MySQL
Python 3.9 or above
Any IDE of your choice
Postman
******************************************************************************************
How to Use:
1. Create a virtual env 
2. Pip install Flask, flask_mysqldb, flask_httpauth
3. Use sql file to create a database
4. Open app.py
5. Replace MySQL setup information to your own MySQL info
6. Run app.py
7. Open postman
8. Use GET, POST, PUT, and DELETE methods to view, add and manipulate the database
******************************************************************************************
Documentation:
get_songs() returns the values present in the songs table
    Format: localhost:5000/songs?format=<can be json or xml>

get_songs_by_id() returns a value present in the songs table
    Format: localhost:5000/songs/<song id>?format=<can be json or xml>

get_songs_by_param() returns a value in the table using specific criteria
    Format: localhost:5000/songs/param?name=<criteria>&param=<paramter for criteria>&format=<can be json, xml, or blank>
    
    ex: localhost:5000/songs/param?name=title&param="my songs"&format=json
        localhost:5000/songs/param?name=release_year&param=1971&format=

add_song() adds a song to the songs table in the database. 
    Format: 
    {
        "title": "song title",
        "artist": "artist name",
        "album": "album title",
        "release_year": year
    }

update_song_by_id() updates information to a song in the database
    Format: localhost:5000/songs/<song id>
    {
        "title": "song title",
        "artist": "artist name",
        "album": "album title",
        "release_year": year
    }

delete_song() deletes a song in the database via song id
    Format: localhost:5000/songs/<song id>