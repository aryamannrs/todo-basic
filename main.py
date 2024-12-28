tasks = []
completed = []


def remove_tasks(tasks):
    if not tasks:
        print("\nNo tasks to remove.")
        return

    print("\nTasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")
    b = int(input("enter the task number you want to remove: ")) -1
    tasks.pop(b)
    print("task removed")
    return
        
def mark_tasks(tasks):
    if not tasks:
        print("\nNo tasks to added.")
        return

    print("\nTasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")
    b = int(input("enter the task number you want to mark: "))
    e = b-1
    c = tasks[e]
    completed.append(c)
    tasks.pop(e)
    print("task marked complete")
    return
    
        


print("1. Add tasks", "2. View Tasks", "3. Remove tasks", "4. Mark task complete", "5. View completed tasks", "6. Exit",sep = "\n")
while True:
    d = int(input("Enter action you want to take: "))
    if d == 1:
        x = input("enter the task you want to add: ")
        print(f"{x} was added to tasks")
        tasks.append(x)
    elif d == 2:
        print(tasks)
        
    elif d == 3:
        remove_tasks(tasks)
        
    elif d == 4:
        mark_tasks(tasks)
        
    elif d == 5:
        print(completed)
        
    elif d == 6:
        break
    else:
        print("invalid command")
    
