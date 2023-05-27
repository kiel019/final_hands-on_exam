from flask import Flask, make_response, jsonify, request
from flaskext.mysql import MySQL

app = Flask(__name__)

#Setting up MySQL
mysql = MySQL(app)
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_PASSWORD'] = 'apzx0dfd6'
app.config['MYSQL_DB'] = 'songlist'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

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
    data = data_fetch("""SELECT * FROM songs""")
    return make_response(jsonify(data), 200)

#GET method to pull songs from table via release year
@app.route("/songs/<int:id>/year", methods=["GET"])
def get_songs_by_year(id):
    data = data_fetch("""SELECT * FROM songs where release_year={}""".format(id))
    return make_response(jsonify({data}), 200)

#Using POST method on the songs directory
@app.route("/songs", methods=['POST'])
def add_song():
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
    cur.close()
    return make_response(jsonify({"message": "Song added successfully"}), 201)

#Run the python file
if __name__ == "__main__":
    app.run(debug=True)