from flask import Flask, jsonify, request
import data

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def aloha_world():
    return "aloha, world!"


# /api/islands


@app.route("/api/islands")
def get_all_islands():
    return jsonify(data.islands)


@app.route("/api/islands/<island_id>")
def get_island_by_id(island_id):
    for island in data.islands:
        if island["id"] == int(island_id):
            return island


# /api/parks


@app.route("/api/parks")
def get_all_parks():
    island = request.args.get('island')
    return jsonify(data.parks)


@app.route("/api/parks/<park_id>")
def get_park_by_id(park_id):
    for park in data.parks:
        if park["id"] == int(park_id):
            return park


app.run(use_reloader=True)
