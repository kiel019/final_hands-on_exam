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

@app.route('/')
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run(debug=True)