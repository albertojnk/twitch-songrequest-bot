import requests
import random
import string
import os 
from flask import Flask, render_template, request
from twitch_songrequest_bot.models import collection

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/twitch/oauth', methods=['post'])
def twitch_oauth():
    scopes = "viewing_activity_read"
    state = get_random_string(32)
    url = "https://id.twitch.tv/oauth2/authorize?client_id=" + os.environ("TWITCH_CLIENT_ID")
    url += "&redirect_uri=" + os.environ("TWITCH_REDIRECT_URI")
    url += "&response_type=code"
    url += "&scope=" + scopes
    url += "&state=" + state
    return requests.get(url).content


@app.route('/api/playlist', methods=['post'])
def playlist():
    link = request.form['link']
    collection.update()
    return f"{link}"

def get_random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

app.run()