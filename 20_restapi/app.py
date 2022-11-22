'''
u2be -- Nakib Abedin, Joseph Jeon
SoftDev
K20 -- Restful APIs
2022-11-21
time spent: 0.7 hrs
'''
from flask import Flask, render_template
import requests

app = Flask(__name__)

key = open('key_nasa.txt')
url = 'https://api.nasa.gov/planetary/apod'
json = requests.get(url, params={'api_key':key}).json()

@app.route('/')
def page():
    return render_template("main.html", title = json['title'], explanation = json['explanation'], imgURL = json['url'])

if __name__ == "__main__":
    app.debug = True 
    app.run()