import requests
import threading
from flask import Flask, request, jsonify, render_template
from bs4 import BeautifulSoup
import random

app = Flask(__name__)

@app.route("/watch-new")
def watch_new():

    r = requests.get('https://anix.to/anime/one-piece-ov8/ep-1')
    if r.status_code == 200:
        doc = BeautifulSoup(r.text, "html.parser")
        divs = doc.find("div", class_="wrapper")
        div = divs.find("div", class_="container watch-wrap")
        d = div.find("div", class_="main-inner")
        fs = d.find("aside", class_="sidebar")
       
        sd = fs.find("div", id="ani-detail-info")
        
        dbs = sd.find("div", class_="ani-data")
        one = dbs.find("div", class_="maindata")
        final = one.find("div", class_="sub-dub-total")
        onepisu = final.find("span", class_="sub")
        ep = int(onepisu.prettify().splitlines()[5])
      
        f = requests.get(f'https://gogoanimehd.to/one-piece-episode-{str(ep)}')
        soup = BeautifulSoup(f.text, 'html.parser')
    
        data = soup.find('div', class_='play-video').find('iframe')["src"]
        down = soup.find('li', class_='dowloads').find('a')['href']
        
       
    
        return render_template('vid.html', vid=data, download=down)
        
    else:
        return jsonify({"error": "FAILED TRY AGAIN LATER"}), 401

@app.route("/current-episodes")
def get_episodes():

    r = requests.get('https://anix.to/anime/one-piece-ov8/ep-1')
    if r.status_code == 200:
        doc = BeautifulSoup(r.text, "html.parser")
        divs = doc.find("div", class_="wrapper")
        div = divs.find("div", class_="container watch-wrap")
        d = div.find("div", class_="main-inner")
        fs = d.find("aside", class_="sidebar")
       
        sd = fs.find("div", id="ani-detail-info")
        
        dbs = sd.find("div", class_="ani-data")
        one = dbs.find("div", class_="maindata")
        final = one.find("div", class_="sub-dub-total")
        onepisu = final.find("span", class_="sub")
        
        data = {    
            "number_of_eps": int(onepisu.prettify().splitlines()[5])   
        }
    
        return jsonify(data), 200
        
    else:
        return jsonify({"error": "FAILED TRY AGAIN LATER"}), 401
        
@app.route("/download/<episode>")
def main_scraper(episode):
    
    r= requests.get(f'https://gogoanimehd.to/one-piece-episode-{episode}')
    soup = BeautifulSoup(r.text, 'html.parser')
    
    data = soup.find('li', class_='doodstream').find('a')["data-video"]
    return jsonify({"doodstream": data}), 200
        
app.run(host='0.0.0.0', port=8080, debug=True)
