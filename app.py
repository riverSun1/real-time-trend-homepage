# 트렌드 홈페이지 개발

# 오늘의유머 https://www.todayhumor.co.kr/
# 클리앙 https://www.clien.net/service/

# set FLASK_DEBUG=true/false

# pip install flask
from flask import Flask, render_template
app = Flask(__name__)

# 크롤링 라이브러리 import
import requests
from bs4 import BeautifulSoup

import trend

@app.route('/')
def hello():
    list_humor, list_humor_href = trend.humor()
    list_clien, list_clien_href = trend.clien()
    return render_template("index.html", 
                           humor = list_humor, 
                           clien = list_clien, 
                           humor_href = list_humor_href, 
                           clien_href = list_clien_href,
                           list_humor_len = len(list_humor),
                           list_clien_len = len(list_clien))

@app.route('/about')
def about():
    return "about World!"

if __name__ == '__main__':
    app.run()