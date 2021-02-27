from flask import Flask

app = Flask(__name__)

stock = {}

@app.route('/stocks', methods=['GET'])
def get_stocks():
    return stock

@app.route('/stocks', methods=['POST'])
def update_stock():
    return "updated"

@app.route('/stock/<stock_id>', methods=['GET'])
def get_stock(stock_id):
    if stock_id in stock.keys():
        return stock[stock_id]
    return stock_id + " not found"

if __name__ == "__main__":
    app.run(debug=True)
