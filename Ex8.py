import requests
import json
import time

response1 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
json_text = response1.text
obj = json.loads(json_text)
token = obj["token"]
time_S = obj["seconds"]

payload = {"token": f"{token}"}
response2 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=payload)
obj2 = json.loads(response2.text)
status =obj2["status"]

if status == "Job is NOT ready":
    print("Статус корректный:", status)

time.sleep(int(time_S))

response3 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=payload)

obj3 = json.loads(response3.text)
status_ready =obj3["status"]
result = obj3["result"]

if status_ready == "Job is ready":
    print("Статус корректный:", status_ready)
if result is not None:
    print("Result присутствует и равен: ", result)
