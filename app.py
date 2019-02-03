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
    avg_sent = (reddit_sent + twitter_sent) / 2000
    final_text = "Error"
    if avg_sent > 0.75:
        final_text = "Overwhelmingly Positive"
    elif avg_sent > 0.3:
        final_text = "Positive"
    elif avg_sent > 0.1:
        final_text = "Slightly Positive"
    elif avg_sent < -0.75:
        final_text = "Overwhelmingly Negative"
    elif avg_sent < -0.3:
        final_text = "Negative"
    elif avg_sent < -0.1:
        final_text = "Slightly Negative"
    else:
        final_text = "Neutral"
    return render_template("result.html", twitter = twitter_sent, reddit = reddit_sent, twitter_high = twitter_extremes["max"], twitter_low = twitter_extremes["min"], reddit_low = reddit_extremes["min"], reddit_high = reddit_extremes["max"], final_text = final_text, text = text)

if __name__ == '__main__':
    app.run(debug=True)
