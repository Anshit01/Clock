from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route("/")
def index():
    now = datetime.datetime.now()
    year, month, date = str(now.date()).split('-')
    hour, minute = str(now.time()).split(':')[0:2]
    return render_template('index.html', date=date, month = month, year = year, hour = hour, minute = minute)



if(__name__  == '__main__'):
    app.run(debug=True)
