import requests

data = {
    "id": 3
}


response = requests.post("http://127.0.0.1:5000/tasks/delete",json=data)
    
print("raw response:" )