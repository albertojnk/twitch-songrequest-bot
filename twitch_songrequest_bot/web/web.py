from flask import Flask, render_template, request
from twitch_songrequest_bot.models import collection

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/api/playlist', methods=['post'])
def playlist():
    link = request.form['link']
    collection.update()
    return f"{link}"

app.run()