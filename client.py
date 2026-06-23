import requests

data = {
    "text": "reverse this text"
}


response = requests.post("http://127.0.0.1:5000/ai",json=data)
    
print(response.json()) 