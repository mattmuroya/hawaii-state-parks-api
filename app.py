import copy
from flask import Flask, jsonify, request
from flask_swagger_ui import get_swaggerui_blueprint
import data
import common

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
app.url_map.strict_slashes = False

SWAGGER_URL = ""
API_URL = "/static/openapi.yml"

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        "app_name": "Hawaii State Parks API"
    }
)

app.register_blueprint(swaggerui_blueprint)


@app.route("/aloha")
def aloha_world():
    return "aloha, world!"


# /api/parks


@app.route("/api/parks")
def get_parks():
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
            common.populate_subdata(park)

        return jsonify(arr)
    except ValueError:
        return {"error": "Invalid query parameters"}, 400


@ app.route("/api/parks/<park_id>")
def get_park_by_id(park_id):
    try:
        for park in data.parks:
            if park["id"] == int(park_id):
                park_copy = copy.deepcopy(park)
                common.populate_subdata(park_copy)
                return park_copy
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
