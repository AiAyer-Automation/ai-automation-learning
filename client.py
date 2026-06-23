import requests

data = {
    "id": 1,
    "task": "Update Now"
}


response = requests.post("http://127.0.0.1:5000/tasks/update",json=data)
    
print("raw response:" )