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
    return twitter.find(text) + " " + reddit.find(text)

if __name__ == '__main__':
    app.run(debug=True)
