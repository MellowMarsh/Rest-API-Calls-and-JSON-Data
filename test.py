# Pulling Song from https://lyrics.ovh Lyrics from an API
import json
import requests

artist = 'Jurassic 5'
song_title = 'Quality Control'
keywords = {'control', 'like'}
url = 'https://api.lyrics.ovh/v1/' + artist + '/' + song_title

# fetch Lyrics
response = requests.get(url)
json_data = json.loads(response.content)
lyrics = json_data['lyrics']

# add lyrics into json format
json.dump(json_data, open('data.json', "w"))

# determine how many times the keywords are used in the song
statistics = {}
for keyword in keywords:
    statistics[keyword] = lyrics.count(keyword)

print(statistics)














print(lyrics)
