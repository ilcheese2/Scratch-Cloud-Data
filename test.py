import requests
import json
import time 
import itertools

items = 200
url = f"https://clouddata.scratch.mit.edu/logs?projectid=12785898&limit={items}&offset=0"

filename = "data.json"

while True:
    time.sleep(1)
    new_data = requests.get(url).json()
    remove = []
    with open(filename) as a:
        data = json.load(a)

    for index, s  in enumerate(new_data):
        for b in data:
            if b["timestamp"] == s["timestamp"]:
                remove.append(index)

    for index in sorted(remove, reverse=True):
        try:
            del new_data[index]
        except IndexError:
            pass

    data.extend(new_data)

    if(len(data) >= 600):
        data = data[200:]

    with open(filename, "w") as a:
        json.dump(data, a, indent=4)
