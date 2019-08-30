from flask import Flask, make_response

app = Flask(__name__)
app.config.from_object('config')
from helper import is_isbn_or_key

@app.route('/book/search/<q><page>')
def search(q, page):
    """
    q:普通关键字 or isbn(一组数字）--如何鉴别
    page:strat count
    :return:
    """
    #isbn13 13个0-9的数字组合
    #isbn10 不怎么用，含有一些' _'

    isbn_or_key = is_isbn_or_key(q)
    pass



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.config['DEBUG'])

