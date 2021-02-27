from flask import Flask
import praw
from praw.models import MoreComments

app = Flask(__name__)
reddit = praw.Reddit(client_id='tLNJPqcv90IWWQ', client_secret='f8viKi1NaK7CAjLX8wv24CAl-DggnQ', user_agent='w4ll-str33t-h4x')

stock = {}

@app.route('/stocks', methods=['GET'])
def get_stocks():
    return stock

@app.route('/stocks', methods=['POST'])
def update_stock():
    posts = reddit.subreddit('wallstreetbets').hot(limit=1000)
    search_str = []
    for post in posts:
        search_str.append(post.title)
    return str(search_str)

@app.route('/stock/<stock_id>', methods=['GET'])
def get_stock(stock_id):
    if stock_id in stock.keys():
        return stock[stock_id]
    return stock_id + " not found"

if __name__ == "__main__":
    app.run(debug=True)
