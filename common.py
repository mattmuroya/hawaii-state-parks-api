from flask import request
import data


def get_param_list(param_name):
    return list(
        map(int, filter(None, (request.args.get(param_name).split(",")))))


def get_island_name_by_id(id_: int):
    for island in data.islands:
        if island["id"] == id_:
            return island["name"]


def get_activity_name_by_id(id_: int):
    for activity in data.activities:
        if activity["id"] == id_:
            return activity["name"]


def park_contains_island_id(park, ids):
    return park["island"] in ids


def park_contains_activity_id(park, ids):
    for id_ in park["activities"]:
        if id_ in ids:
            return True
