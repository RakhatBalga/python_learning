import os
import pandas as pd

CSV_FILE = "tasks.csv"


print("Welcome to your Todo List!\n")

def load_tasks():

    if os.path.exists(CSV_FILE):
        return pd.read_csv(CSV_FILE)
    else: 
        return pd.DataFrame(columns=["task", "status"])

def add_task(new_task):
    df = load_tasks()

    new_row = pd.DataFrame([{"task": new_task, "status": "pending"}])
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv(CSV_FILE, index=False)

def view_tasks():
    df = load_tasks()

    if df.empty:
        print("Your todo list is empty\n")
    else: 
        print(df.to_string(index=False))

def delete_task(task_number):
    df = load_tasks()

    try: 
        df = df.drop(task_number).reset_index(drop=True)
        df.to_csv(CSV_FILE, index=False)
        print("Task was deleted")

    except Exception as e:
        print(f"Task not found! {e}")

# def complete_task(task_number):
#     df = load_tasks()

#     try:
#         df.loc[task_number, "status"] = "completed"
#         df.to_csv(CSV_FILE, index=False)
#         print("Task was completed")
#     except Exception as e:
#         print(f"Task not found! {e}")

def completed_task(task_number):
    df = load_tasks()

    try: 
        df.loc[task_number, "status"] = "completed"
        df.to_csv(CSV_FILE, index=False)
        print("Task was completed")
    except Exception as e:
        print(f"Task not found! {e}")

def main():
    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose: ")

        if choice == "1":
            task = input("Enter task: ")
            add_task(task)
            view_tasks()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            task_number = int(input("Enter task number to complete: "))
            completed_task(task_number)
        elif choice == "4":
            task_number = int(input("Enter task number to delete: "))
            delete_task(task_number)
        elif choice == "5":
            break
        else: 
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
     
