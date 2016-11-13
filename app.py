from flask import Flask
from flask import request
from flask import render_template
import trends

app = Flask(__name__)
trend_object = None

@app.route('/')
def my_form():
    global trend_object
    trend_object = trends.Trends("calhackstrends@gmail.com", "go_bears")
    return render_template("index.html")

@app.route('/fintrends', methods=['POST'])
def my_form_post():
    global trend_object
    text = request.form['text']
    datestart = request.form['datestart']
    start_split = datestart.split('-')
    dateend = request.form['dateend']
    end_split = dateend.split('-')
    vals = trend_object.getTrendData(text, start_split[1]+"/"+start_split[0], end_split[1]+"/"+end_split[0])
    print([v.getValue() for v in vals])
    return

if __name__ == '__main__':
    app.run()
