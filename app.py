from flask import Flask
app = Flask(__name__)


@app.route("/")
def aloha_world():
    return "aloha, world!"


app.run(use_reloader=True)
