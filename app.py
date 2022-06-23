import copy
from flask import Flask, jsonify, request
import data
import common

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
app.url_map.strict_slashes = False


@app.route("/")
def aloha_world():
    return "aloha, world!"


# /api/parks


@app.route("/api/parks")
def get_all_parks():
    try:
        arr = copy.deepcopy(data.parks)

        if request.args.get("islands"):
            island_ids = common.get_param_list("islands")
            arr = list(
                filter((lambda park: common.park_contains_island_id(park, island_ids)), arr))

        if request.args.get("activities"):
            activity_ids = common.get_param_list("activities")
            arr = list(
                filter((lambda park: common.park_contains_activity_id(park, activity_ids)), arr))

        for park in arr:
            park["island"] = common.get_island_name_by_id(park["island"])
            park["activities"] = list(
                map(common.get_activity_name_by_id, park["activities"]))

        return jsonify(arr)
    except ValueError:
        return {"error": "Invalid query parameters"}, 400


@ app.route("/api/parks/<park_id>")
def get_park_by_id(park_id):
    try:
        for park in data.parks:
            if park["id"] == int(park_id):
                return park
        return {"error": "Park ID not found"}, 404
    except ValueError:
        return {"error": "Invalid park ID"}, 400


# /api/activities


@ app.route("/api/activities")
def get_all_activities():
    return jsonify(data.activities)


# /api/islands


@ app.route("/api/islands")
def get_all_islands():
    return jsonify(data.islands)


# run


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
