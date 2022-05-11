from flask import Flask
from flask import render_template
from flask import request
import traceback

app = Flask(__name__)

@app.route("/")
def ask_num():
    return render_template("index.html")

@app.route("/result", methods=["GET"])
def is_prime():
    n = request.args.get("value","")
    try:
        if int(n)%2 == 0:
            s = "偶数"
        else:
            s = "奇数"
    except:
        e = traceback.format_exc()
        return render_template("error.html", error=e)
    return render_template("result.html", n=n, s=s)
