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
    return render_template("result.html", twitter = twitter_sent, reddit = reddit_sent, twitter_high = twitter_extremes["max"], twitter_low = twitter_extremes["min"], reddit_low = reddit_extremes["min"], reddit_high = reddit_extremes["max"])

if __name__ == '__main__':
    app.run(debug=True)
