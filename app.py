from flask import Flask, request, render_template

from pyscripts import reddit
from pyscripts import twitter

app = Flask(__name__)

@app.route('/')
def result():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def form_post():
    text = request.form['text']
    reddit_sent, reddit_extremes = reddit.find(text)
    twitter_sent, twitter_extremes = twitter.find(text)
    return render_template("result.html", twitter = twitter_sent, reddit = reddit_sent)

if __name__ == '__main__':
    app.run(debug=True)
