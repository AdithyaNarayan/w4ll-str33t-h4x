from flask import Flask, render_template
from flask import jsonify
import praw
from praw.models import MoreComments
from os.path import join, dirname, realpath

app = Flask(__name__)
reddit = praw.Reddit(client_id='', client_secret='', user_agent='w4ll-str33t-h4x')

stock = {}

@app.route('/', methods=['GET'])
def update_stock():
    posts = reddit.subreddit('wallstreetbets').hot(limit=1000)
    search_str = ""
    for post in posts:
        search_str += post.title
    
    f = open(join(dirname(realpath(__file__)),"..", "stocks\\stocks.txt"), "r")
    for line in f.readlines():
        code = line.split('-')[0].strip()
        if len(code) < 3:
            continue
        num = search_str.count(code)
        if num > 0:
            stock[code] = num

    stocks = sorted(stock.items(), key=lambda keyvaluepair: -keyvaluepair[1])
    
    return render_template('index.html', stocks=stocks[:10])


@app.route('/stonks', methods=['GET'])
def update_stonk():
    stocks = [('AMC', 15), ('GME', 10),('AMC', 15), ('GME', 10),('AMC', 15), ('GME', 10),('AMC', 15), ('GME', 10),('AMC', 15), ('GME', 10)]
    return render_template('index.html', stocks=stocks[:10])

if __name__ == "__main__":
    app.run(debug=True)
