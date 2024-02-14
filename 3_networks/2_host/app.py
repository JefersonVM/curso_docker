import flask
from flask import request, json, jsonify
import requests
import psycopg2
from psycopg2.extras import RealDictCursor

app = flask.Flask(__name__)
app.config["DEBUG"] = True

app.config['DB_HOST'] = 'host.docker.internal'
app.config['DB_USER'] = 'postgres'
app.config['DB_PASSWORD'] = '18020526'
app.config['DB_NAME'] = 'flaskhost'

def get_db():
    conn = psycopg2.connect(
        dbname=app.config['DB_NAME'],
        user=app.config['DB_USER'],
        password=app.config['DB_PASSWORD'],
        host=app.config['DB_HOST']
    )
    return conn

@app.route("/", methods=["GET"])
def index():
    data = requests.get('https://randomuser.me/api')
    return data.json()

@app.route("/inserthost", methods=['POST'])
def inserthost():
    data = requests.get('https://randomuser.me/api').json()
    username = data['results'][0]['name']['first']

    conn = get_db()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("""INSERT INTO users(name) VALUES(%s)""", (username,))
    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
