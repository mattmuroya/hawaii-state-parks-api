# quick utility to get the park names and ids for documentation

import requests

res = requests.get(
    "https://hawaii-state-parks-api.herokuapp.com/api/parks")

for x in res.json():
    print("| " + str(x["id"]) + " | " + x["name"] + " | ")
