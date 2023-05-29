from flask import Flask, make_response, jsonify, Response, request
from flaskext.mysql import MySQL
from flask_mysqldb import MySQL
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
fmt = "json"
auth = HTTPBasicAuth()

USER_DATA = {"admin": "admin"}

@auth.verify_password
def verify(username, password):
    if not (username and password):
        return False
    return USER_DATA.get(username) == password

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
@auth.login_required
def get_songs():
    try:
        data = data_fetch("""SELECT * FROM songs""")
        fmt = request.args.get('format')
        myResponse = make_response(jsonify(data))
        if fmt.lower() == "xml":
            myResponse.mimetype = 'xml'
        else:
            myResponse.mimetype = 'json'
        return myResponse
    except Exception as ex:
        print(ex)

#GET method to pull one entry from table using song id
@app.route("/songs/<int:id>", methods=["GET"])
@auth.login_required
def get_songs_by_id(id):
    try:
        data = data_fetch("""SELECT * FROM songs WHERE id = {}""".format(id))
        fmt = request.args.get('format')
        myResponse = make_response(jsonify(data))
        if fmt.lower() == "xml":
            myResponse.mimetype = 'xml'
        else:
            myResponse.mimetype = 'json'
        return myResponse
    except Exception as ex:
        print(ex)
    

#GET method to pull an entry from table using parameters
@app.route("/songs/param", methods=["GET"])
@auth.login_required
def get_songs_by_param():
    try:
        _name = request.args.get('name')
        _param = request.args.get('param')
        if _name == "id":
            data = data_fetch("""SELECT * FROM songs WHERE id ={}""".format(_param))
        elif _name == "release_year":
            data = data_fetch("""SELECT * FROM songs WHERE release_year ={}""".format(_param))
        elif _name == "title":
            data = data_fetch("""SELECT * FROM songs WHERE title ={}""".format(_param))
        elif _name == "artist":
            data = data_fetch("""SELECT * FROM songs WHERE artist ={}""".format(_param))
        elif _name == "album":
            data = data_fetch("""SELECT * FROM songs WHERE album ={}""".format(_param))
        fmt = request.args.get('format')
        myResponse = make_response(jsonify(data))
        if fmt.lower() == "xml":
            myResponse.mimetype = 'xml'
        else:
            myResponse.mimetype = 'json'
        return myResponse
    except Exception as ex:
        print(ex)

#Using POST method on the songs directory
@app.route("/songs", methods=['POST'])
@auth.login_required
def add_song():
    try:
        cur = mysql.connection.cursor()
        json = request.get_json(force=True)
        title = json["title"]
        artist = json["artist"]
        album = json["album"]
        release_year = json['release_year']
        cur.execute(
            """ INSERT INTO songs (title, artist, album, release_year) VALUE (%s, %s, %s, %s)""", (title, artist, album, release_year),
        )
        mysql.connection.commit()
        _response = jsonify("Song added successfully!")
        _response.status_code = 200
        return _response
    except Exception as ex:
        print(ex)
    finally:
        cur.close()


#Use PUT method to update a song in database
@app.route("/songs/<int:id>", methods=["PUT"])
@auth.login_required
def update_song_by_id(id):
    try:
        cur = mysql.connection.cursor()
        json = request.get_json(force=True)
        title = json["title"]
        artist = json["artist"]
        album = json["album"]
        release_year = json["release_year"]
        sqlQuery = " UPDATE songs SET title = %s, artist = %s, album = %s, release_year = %s WHERE id = %s"
        bindData = (title, artist, album, release_year, id)
        cur.execute(sqlQuery, bindData)
        mysql.connection.commit()
        _response = jsonify("Song updated successfully!")
        _response.status_code = 200
        return _response
    except Exception as ex:
        print(ex)
    finally:
        cur.close()
        
        
    

#Use DELETE method to remove a song in the database
@app.route("/songs/<int:id>", methods=["DELETE"])
@auth.login_required
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

#Run the python file
if __name__ == "__main__":
    app.run(debug=True)