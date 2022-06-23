from flask import request
import data


def get_param_list(param_name):
    return list(
        map(int, filter(None, (request.args.get(param_name).split(",")))))


def get_island_name_by_id(id: int):
    for island in data.islands:
        if island["id"] == id:
            return island["name"]


def get_activity_name_by_id(id: int):
    for activity in data.activities:
        if activity["id"] == id:
            return activity["name"]


def park_contains_island_id(park, ids):
    return park["island"] in ids


def park_contains_activity_id(park, ids):
    for id in park["activities"]:
        if id in ids:
            return True
