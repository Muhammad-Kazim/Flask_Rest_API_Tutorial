import requests

BASE = "http://127.0.0.1:5000/"

response = requests.put(BASE + "video/27", {"name": "Kazim", "views": 45, "likes": 19})

print(response.json())
