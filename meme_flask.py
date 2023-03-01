from flask import Flask,render_template
import requests
import json

app = Flask(__name__)

def get_meme():
    url = "https://meme-api.com/gimme"
    response = json.loads(requests.request("GET", url).text)
    meme_large = response["preview"][-2]
    title = response["title"]
    return meme_large,title

@app.route("/")
def index():
    url,title = get_meme()
    return render_template("meme_index.html",url=url,title=title)

app.run(host="0.0.0.0",port=80)