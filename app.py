
from flask import Flask, render_template, request
from main import *

# download nltk


#Start Chatbot
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/record")
def get_bot_response():
    text = dengerin()
    bilang(text)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=5500)