import requests

data = [
    {"name": "Kazim", "views": 307, "likes": 555},
    {"name": "Wajiha", "views": 145, "likes": 2222},
    {"name": "Zulfiqar", "views": 205, "likes": 789}
]

BASE = "http://127.0.0.1:5000/"

print('PUT REQUEST /n')
for i, x in enumerate(data):
    response = requests.put(BASE + f"video/{i}", x)
    print(response.json())

input()
print('GET REQUEST /n')
for i, x in enumerate(data):
    response = requests.get(BASE + f"video/{i}", x)
    print(response.json())


input()
response = requests.delete(BASE + f"video/{1}")
print(response)

print('GET REQUEST AFTER DELETE/n')
for i, x in enumerate(data):
    response = requests.get(BASE + f"video/{i}", x)
    print(response.json())

input()
print('PATCH REQUEST')

response = requests.patch(BASE + f"video/{2}", {"name": "Zulfi"})
print(response.json())
