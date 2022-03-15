from flask import Flask, render_template, request, redirect, url_for
from sqla_wrapper import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy("sqlite:///db.sqlite")


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String, unique=False)
    text = db.Column(db.String, unique=False)


db.create_all()


@app.route("/")
def index():
    return render_template("lol.html")


@app.route("/add-message", methods=["Post"])
def add_message():
    username = request.form.get("username")
    text = request.form.get("text")

    message = Message(author=username, text=text)
    message.save()

    return redirect("/")


if __name__ == "__main__":
    app.run()
