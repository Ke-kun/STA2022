from flask import Flask
from flask import render_template
from flask import request
import traceback
import math

app = Flask(__name__)

title = "課題2:素数判定"


def is_prime(n):
    if n == 1:
        return "合成数"

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return "合成数"

    return "素数"


@app.route("/")
def ask_num():
    return render_template("index.html", title=title)


@app.route("/result", methods=["GET"])
def prime():
    n = request.args.get("value", "")
    try:
        s = is_prime(int(n))
    except:
        e = traceback.format_exc()
        return render_template("error.html", title=title, error=e)
    return render_template("result.html", title=title, n=n, s=s)
