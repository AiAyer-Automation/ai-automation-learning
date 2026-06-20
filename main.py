import json

FILE = "tasks.json" 
print("gi")
def load_tasks():
    try:
        with open(FILE,"r") as f:
            return json.load(f)
    except:
        return []
    

def save_tasks(tasks):
    with open(FILE, "w" ) as f:
        json.dump(tasks, f)


def show_tasks(tasks):
    print("\ntasks:")
    for i, t in enumerate(tasks):
        print( f"{i+1}. {t}")


def main():
    print("main")
    tasks = load_tasks()
    while True:
     print("\n1- Add task")
     print("2- Show tasks")
     print("3- Delete task")
     print("4- Exit")

     choice = input("Choose: ")

     if choice == "1":
        task = input("New task: ")
        tasks.append(task)
        save_tasks(tasks)

     elif choice == "2":
        show_tasks(tasks)

     elif choice == "3":
        show_tasks(tasks)
        index = int(input("Number to delete: ")) - 1

        if 0 <= index < len(tasks):
            tasks.pop(index)
            save_tasks(tasks)

     elif choice == "4":
         break


main()