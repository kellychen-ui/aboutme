from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    link = "<h1>歡迎進入陳宜琳的網站首頁</h1>"
    link += "<a = href=/mis>課程</a><hr>"
    link += "<a href=/today>今天日期</a><hr>"
    link += "<a href=/about>關於宜琳</a><hr>"
    return link

@app.route("/mis")
def course():
    return "<h1>資訊管理導論</h1>"

@app.route("/today")
def today():
    now = datetime.now()
    year = str(now.year) #取得年份
    month = str(now.month) #取得月份
    day = str(now.day) #取得日期
    now = year + "/" + month + "/" + day
    return render_template("today.html", datetime = str(now))
@app.route("/about")
def about():
    return render_template("abou8-2.html")

if __name__ == "__main__":
    app.run(debug=True)

