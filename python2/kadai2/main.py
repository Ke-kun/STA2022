from flask import Flask
from flask import render_template
from flask import request
import traceback

app = Flask(__name__)
title = "課題2:素数判定"

@app.route("/")
def ask_num():
    return render_template("index.html", title=title)

@app.route("/result", methods=["GET"])
def is_prime():
    n = request.args.get("value","")
    try:
        if int(n)%2 == 0:
            s = "偶数"
        else:
            s = "素数"
    except:
        e = traceback.format_exc()
        return render_template("error.html", title=title, error=e)
    return render_template("result.html", title=title, n=n, s=s)
