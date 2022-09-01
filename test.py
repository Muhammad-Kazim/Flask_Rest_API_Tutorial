import requests

data = [
    {"name": "Kazim", "views": 307, "likes": 555},
    {"name": "Wajiha", "views": 145, "likes": 2222},
    {"name": "Zulfiqar", "views": 205, "likes": 789}
]

BASE = "http://127.0.0.1:5000/"

for i, x in enumerate(data):
    response = requests.put(BASE + f"video/{i}", x)
    print(response.json())

input()

response = requests.delete(BASE + f"video/{1}")
print(response)

input()

response = requests.get(BASE + f"video/{0}")
print(response.json())
