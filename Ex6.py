import requests

response = requests.post("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)
first_response = response.history[0]
response2 = response.history[1]
response3 = response.history[2]
end = response

print(first_response.url)
print(response2.url)
print(response3.url)
print(end.url)