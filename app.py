from flask import Flask, make_response, jsonify, request
from flaskext.mysql import MySQL

app = Flask(__name__)

#Setting up MySQL
mysql = MySQL(app)
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_PASSWORD'] = 'apzx0dfd6'
app.config['MYSQL_DB'] = 'mydatabase'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

