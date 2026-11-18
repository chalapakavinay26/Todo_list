def show_menu():
    print("\n---(To-Do List App) ---")
    print("1. (View Tasks)")
    print("2. (Add Task)")
    print("3. (Delete Task)")
    print("4. (Exit)")

def todo_app():
    tasks = []
    while True:
        show_menu()
        choice = input("your option entered (1-4): ")
        
        if choice == '1':
            if not tasks:
                print("\nno task found! (No tasks found.)")
            else:
                print("\n--- your task ---")
                for index, task in enumerate(tasks, 1):
                    print(f"{index}. {task}")
                    
        elif choice == '2':
            task = input("new task added: ")
            if task.strip():
                tasks.append(task)
                print(f"'{task}' successfully added!")
            else:
                print("please enter work number.")
                
        elif choice == '3':
            if not tasks:
                print("\nremove no work!")
            else:
                print("\n--- your work folder ---")
                for index, task in enumerate(tasks, 1):
                    print(f"{index}. {task}")
                try:
                    task_num = int(input("removed work number entered: "))
                    if 1 <= task_num <= len(tasks):
                        removed = tasks.pop(task_num - 1)
                        print(f"'{removed}' successfully removed!")
                    else:
                        print("wrong number entered.")
                except ValueError:
                    print("please entered the only number.")
                    
        elif choice == '4':
            print("programing completed. good job!")
            break
        else:
            print("wrong option entered. 1 to 4 middle selected.")

if __name__ == "__main__":
    todo_app()
