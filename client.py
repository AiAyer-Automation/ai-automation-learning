import requests

data = {
    "name": "Alice"
}

response = requests.post("http://127.0.0.1:5000/api/hello",json=data)

print("raw response:" )
print(response.text)