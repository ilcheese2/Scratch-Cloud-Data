import requests
import json
items = 10
url = f"https://clouddata.scratch.mit.edu/logs?projectid=403845454&limit={items}&offset=0"
data = requests.get(url).json()
filename = "data.json"
with open(filename, "w") as a:
    json.dump(data, a, indent=4)
