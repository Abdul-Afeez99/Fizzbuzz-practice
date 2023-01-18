from flask import *

app = Flask(__name__)


@app.get("/fizzbuzz")
def fizbuzz():
    numbers = list(range(101))
    return render_template("index.html", numbers = numbers)