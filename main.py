import helper
from flask import Flask, request, Response, render_template, redirect, url_for
app = Flask(__name__)

#Definieren auf welche URL die Applikation reagiert
@app.route("/")
def index():
    items = helper.get_all()
    return render_template('index.html', items=items)


@app.route('/add', methods=["POST"])
def add():
    text = request.form.get("text")
    helper.add(text)
    return redirect(url_for("index"))

#Daten werden an index.html übertragen
@app.route('/update/<int:index>')
def update(index):
    helper.update(index)
    return redirect(url_for("index"))