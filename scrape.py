import requests
import json
from bs4 import BeautifulSoup

url = "https://open.spotify.com/playlist/37i9dQZF1EpoYp9UOFfh3m?si=3415a4bd71c04aa2"

r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')
#Find songs heading
songTag = soup.find("div", attrs="tracklist-col position-outer")


# find the parent section of tag
songSection = songTag.find_parent("div")


#find all list items 
songs = songSection.findAll("div", attrs="top-align track-name-wrapper")


song = songs[0]
#iterate through the list and extract data
for song in songs:
    aTag = song.find("a")
    # songLink = aTag["href"]
    songName = song.find("span").text
    songArtist = aTag.find("span").text

script = soup.find_all('script')[6].text.strip()[35:-1]
# print(script)
data = json.loads(script)
items = []
allSongDetails = []
for item in data['tracks']['items']:
    thumbnail = item['track']['album']['images'][0]['url']
    link = item['track']['uri'].strip()[14:]
    name = item['track']['name']
    preview = item['track']['preview_url']
    
    # print(preview)
    
    # print(names)
    songDetails = {
        'title' : name,
        'thumbnail': thumbnail,
        'link' : link,
        'preview' : preview,
    }

    allSongDetails.append(songDetails)


with open("onRepeat.json", "w") as a:
    json.dump(allSongDetails, a)
