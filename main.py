from flask import Flask, render_template, request, redirect
from sqla_wrapper import SQLAlchemy
from uuid import uuid4
import os

app = Flask(__name__)

# Message baza 
db = SQLAlchemy("sqlite:///sqlite.db")

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String, unique=False)
    text = db.Column(db.String, unique=False)


#Uporabnik baza
db = SQLAlchemy(os.getenv("DATABASE_URL", "sqlite:///localhost.sqlite"))

# Naredi bazo s podatki uporabnika
class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String(length=20))

db.create_all()

# Začetna stran
@app.route("/")
def main():
    render_template("main.html")

# Signup stran - pridobimo username in password 
@app.route("/signup", methods=["POST"])
def signup():
    username = request.form.get("username") 
    password = request.form.get("password")

    user = User(id=id, username=username, password=password)


    return render_template("login.html", user)

# CHAT

@app.route("/chat", methods=["GET"])
def index():

    messages = db.query(Message).all()

    return render_template("chat.html", messages=messages)


@app.route("/add-message", methods=["POST"])
def add_message():
    username = request.form.get("username")
    text = request.form.get("text")

    message = Message(author=username, text=text)
    message.save()

    return redirect("/chat")


if __name__ == "__main__":
    app.run()