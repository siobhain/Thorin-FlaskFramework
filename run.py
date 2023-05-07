import os
from flask import Flask

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
    return "Hello, Flask"
    
# __main__ is name od default module in python
if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
