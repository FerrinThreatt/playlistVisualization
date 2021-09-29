import json
from jinja2 import Environment, FileSystemLoader

with open("onRepeat.json", "r") as f:
    albums = json.load(f)

fileLoader = FileSystemLoader("templates")
env = Environment(loader = fileLoader)

rendered = env.get_template("gallery.html").render(albums= albums, title="On Repeat Playlist Visualization")

#write to file

fileName = 'index.html'

with open(f"./site/{fileName}", "w") as f:
    f.write(rendered)
