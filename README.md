# One-Piece-Server
a free private one piece server/api. You can only watch the latest episodes of one piece with this. I made this because gear 5 might break the internet ngl.

# Note: This might not work sometimes. I have never worked with Beautifulsoup before, so this is just a simple script I wrote after reading the docs for the first time. 

# What to do?
- if you are using repl it:
     - {repl_it_website_url}/watch-new ( to watch the recent episode )
     - {repl_it_website_url}/current-episodes ( returns a [JSON](https://www.json.org/json-en.html) data with the amount of episodes one piece has )
     - {repl_it_website_url}/download/<episode> ( params: episode: [str](https://docs.python.org/3/library/stdtypes.html#str). Gives a download url)
- If you are using your local host:
     - Most likely your local host will be ```http://127.0.0.1:8080```
        - {your_local_host}/watch-new ( to watch the recent episode )
        - {your_local_host}/current-episodes ( returns a [JSON](https://www.json.org/json-en.html) data with the amount of episodes one piece has )
        - {your_local_host}/download/<episode> ( params: episode: [str](https://docs.python.org/3/library/stdtypes.html#str). Gives a download url)
      
