from flask import Flask
from flask import jsonify
import praw
from praw.models import MoreComments

app = Flask(__name__)
reddit = praw.Reddit(client_id='tLNJPqcv90IWWQ', client_secret='f8viKi1NaK7CAjLX8wv24CAl-DggnQ', user_agent='w4ll-str33t-h4x')

stock = {}

@app.route('/stocks/<num>', methods=['GET'])
def get_stocks(num):
    try:
        no_of_stocks = int(num)
        stocks = sorted(stock.items(), key=lambda keyvaluepair: -keyvaluepair[1])
        return jsonify(stocks[:no_of_stocks])
    except:
        return "error"

@app.route('/stocks', methods=['POST'])
def update_stock():
    posts = reddit.subreddit('wallstreetbets').hot(limit=1000)
    search_str = ""
    for post in posts:
        search_str += post.title
    
    f = open("stocks/stocks.txt", "r")
    for line in f.readlines():
        code = line.split('-')[0].strip()
        if len(code) < 3:
            continue
        num = search_str.count(code)
        if num > 0:
            stock[code] = num
    
    return "updated"

if __name__ == "__main__":
    app.run(debug=True)
