"""A simple Flask app for retrieving grammar-related song information"""
import os
import requests
from flask import Flask
from flask_restful import Resource, Api
from textblob import TextBlob

app = Flask(__name__)
api = Api(app)

LYRICS_API_URL = os.environ.get('LYRICS_API_URL', 'https://api.lyrics.ovh/v1')
PORT = os.environ.get('PORT', 8080)


@app.route('/healthz')
def healthz():
    """Return a simple health check"""
    return "You're up"


def get_lyrics(artist, song):
    """Fetch the lyrics from the upstream URL"""
    try:
        lyrics_get = requests.get('{}/{}/{}'.format(LYRICS_API_URL,
                                                    artist, song))
    except requests.exceptions.RequestException as e:
        print(e)
    return lyrics_get.json()


def find_part_of_speech(lyrics_json, part_of_speech):
    blob = TextBlob(lyrics_json['lyrics'])
    if part_of_speech in ('VB', 'JJ'):
        return [x[0] for x in blob.tags if part_of_speech in x[1]]
    else:
        print('Part of speech not properly defined')


class GetVerbs(Resource):
    """Create a path to get just the verbs in a song"""
    def get(self, verb_artist, verb_song):
        verbs = find_part_of_speech(get_lyrics(verb_artist, verb_song), 'VB')
        return {'verbs': verbs}


class GetAdjectives(Resource):
    """Create a path to get just the adjectives in a song"""
    def get(self, adjective_artist, adjective_song):
        adjectives = find_part_of_speech(get_lyrics(adjective_artist,
                                                    adjective_song), 'JJ')
        return {'adjectives': adjectives}


api.add_resource(GetVerbs, '/verbs/<string:verb_artist>/<string:verb_song>')
api.add_resource(
    GetAdjectives,
    '/adjectives/<string:adjective_artist>/<string:adjective_song>'
)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
