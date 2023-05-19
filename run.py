import os
import json
from flask import Flask, render_template

# create instance of Flask class called app
# __name is built in python var#
# 1st argument in Flask class is name of applicaiton ie our package
# Flask needs to know where to look for template and static files

app = Flask(__name__)

# use app.route decorator, decorator starts with @ also called pir-notation
# sdecorator is way of wrapping functions
# all functs are objects and can be passded around
# so browse the root dir as indicated by "/"


@app.route("/")
def index():
    # return "<h1>Hello</h1> <h2> Flask </h2>"
    return render_template("index.html")


@app.route("/about")
def about():
    data = []
    with open("data/people.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="AboutPage", people=data)


@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}
    with open("data/people.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    return render_template("member.html", member=member)


@app.route("/contact")
def contact():
    return render_template("contact.html", page_title="ContactUs")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Come Work  For US ")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
