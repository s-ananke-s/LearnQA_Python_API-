import requests

response2 = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(response2.text)

payload_head = {"method":"HEAD"}
response3 = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type", data=payload_head)
print(response3.text)

payload_post = {"method":"POST"}
response1 = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data=payload_post)
print(response1.text)


real_requests = ["GET", "POST", "PUT", "DELETE"]

for i in range(len(real_requests)):
    methods_requests = real_requests[i]
    print(methods_requests)
    if real_requests[i] == "GET":
        for j in range(len(real_requests)):
            payload = {"method": real_requests[j]}
            response=requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=payload)
            print(response.text)
    else:
        for j in range(len(real_requests)):
            payload = {"method": real_requests[j]}
            response = requests.request(methods_requests, "https://playground.learnqa.ru/ajax/api/compare_query_type", data=payload)
            print(response.text)

