# Pulling Song from https://lyrics.ovh Lyrics from an API
import json
import requests

artist = 'Jurassic 5'
song_title = 'Quality Control'
keywords = {'mood'}
url = 'https://api.lyrics.ovh/v1/' + artist + '/' + song_title

# fetch Lyrics
response = requests.get(url)
json_data = json.loads(response.content)
lyrics = json_data['lyrics']

# add lyrics into json format
json.dump(json_data, open('data.json', "w"))














print(lyrics)
