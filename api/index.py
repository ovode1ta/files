from flask import Flask, render_template, send_from_directory
import datetime
import json
from urllib.parse import unquote

def load_songs():
    with open("api/songs.json", 'r', encoding='utf-8') as playlist:
        songs = json.load(playlist)
    return songs

songs = load_songs()



app = Flask(__name__)

@app.route('/')
def home():
    date = int(datetime.datetime.now().strftime("%d")) - 1

    sootd = songs['songs'][date]
    return render_template('index.html', sootd = sootd)

@app.route('/songs/<path:filename>')
def serve_audio(filename):
    return send_from_directory('songs', unquote(filename))

@app.route('/songs.json')
def songsList():
    return send_from_directory('', 'songs.json')

if __name__ == '__main__':
    app.run(debug=True, port="8080")