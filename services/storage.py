import json

FILE = "data.json"

def load_tasks():
    try:
        with open(FILE,"r") as f:
            return json.load(f)
    except:
        return []
    
def save_tasks(tasks):
    with open(FILE, "w" ) as file:
        json.dump(tasks, file , indent=4)
    