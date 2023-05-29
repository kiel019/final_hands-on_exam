from flask import Flask, make_response, jsonify, request
from flaskext.mysql import MySQL
from flask_mysqldb import MySQL

app = Flask(__name__)
_format = "json"

#MySQL Setup
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_PASSWORD'] = 'apzx0dfd6'
app.config['MYSQL_DB'] = 'songlist'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)

#Root directory
@app.route('/')
def hello_world():
    return "<p>This is my Songlist!</p>"

#Data inquiry method
def data_fetch(query):
    cur = mysql.connection.cursor()
    cur.execute(query)
    data = cur.fetchall()
    return data

#GET method to pull songs from the table
@app.route("/songs", methods=["GET"])
def get_songs():
    try:
        data = data_fetch("""SELECT * FROM songs""")
        if (_format == "json"):
            return make_response(jsonify(data), 200)
        elif (_format == "xml"):
            return make_response()
    except Exception as ex:
        print(ex)

#GET method to pull one entry from table using song id
@app.route("/songs/<int:id>", methods=["GET"])
def get_songs_by_id(id):
    try:
        data = data_fetch("""SELECT * FROM songs WHERE id = {}""".format(id))
        return make_response(jsonify(data), 200)
    except Exception as ex:
        print(ex)
    

#Using POST method on the songs directory
@app.route("/songs", methods=['POST'])
def add_song():
    try:
        cur = mysql.connection.cursor()
        json = request.get_json()
        title = json["title"]
        artist = json["artist"]
        album = json["album"]
        release_year = json['release_year']
        cur.execute(
            """ INSERT INTO songs (title, artist, album, release_year) VALUE (%s, %s, %s, %s)""", (title, artist, album, release_year),
        )
        mysql.connection.commit()
        return make_response(jsonify({"message": "Song added successfully"}), 201)
    except Exception as ex:
        print(ex)
    finally:
        cur.close()


#Use PUT method to update a song in database
@app.route("/songs/<int:id>", methods=["PUT"])
def update_song_by_id(id):
    try:
        cur = mysql.connection.cursor()
        json = request.get_json()
        title = json["title"]
        artist = json["artist"]
        album = json["album"]
        release_year = json["release_year"]
        sqlQuery = " UPDATE songs SET title = %s, artist = %s, album = %s, release_year = %s WHERE id = %s"
        bindData = (title, artist, album, release_year, id)
        cur.execute(sqlQuery, bindData)
        mysql.connection.commit()
        return make_response(jsonify({"message": "song updated successfully"}), 204)
    except Exception as ex:
        print(ex)
    finally:
        cur.close()
    

#Use DELETE method to remove a song in the database
@app.route("/songs/<int:id>", methods=["DELETE"])
def delete_song(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute(""" DELETE FROM songs WHERE id = %s""", (id,))
        mysql.connection.commit()
        return make_response(jsonify({"message": "song deleted successfully"}), 200)
    except Exception as ex:
        print(ex)
    finally:
        cur.close()
    

@app.route("/songs/format", methods=["GET"])
def get_params():
    fmt = request.args.get('id')
    return make_response(jsonify({"format": fmt}),200)

#Run the python file
if __name__ == "__main__":
    app.run(debug=True)