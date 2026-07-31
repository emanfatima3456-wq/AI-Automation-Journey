import json
json_string='{"Name": "fatima", "age": 20, "city": "pakistan"}'
data=json.loads(json_string)
print(data["Name"])
print(data["age"])
print(data["city"])
import requests
url="https://official-joke-api.appspot.com/random_joke"
response=requests.get(url)
print(response.json())
print("Status code:",response.status_code)
print("full response:",response.json())

import requests
url="https://official-joke-api.appspot.com/random_joke"
response=requests.get(url)
data=response.json()
print("Joke:")
print("Q:", data["setup"])
print("A:", data["punchline"])
import requests

print("=== 3 Random Jokes ===\n")

for i in range(3):
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    data = response.json()

    print(f"Joke {i+1}:")
    print(f"Q: {data['setup']}")
    print(f"A: {data['punchline']}")
    print()


