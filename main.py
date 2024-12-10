import csv
import os
from datetime import datetime
from collections import defaultdict
import matplotlib.pyplot as plt

# File to store tasks
FILENAME = "tasks.csv"
def load_tasks_from_csv():
    tasks = []
    if os.path.exists(FILENAME):
        with open(FILENAME, mode="r", newline="") as file:
            reader = csv.reader(file)
            tasks = [row for row in reader]
    return tasks

def save_tasks_to_csv(tasks):
    with open(FILENAME, mode="w", newline="") as file:
        writer = csv.writer(file)
        for task, date in tasks:
            writer.writerow([task, date])

def display_menu():
    print("\n====== TO-DO LIST MENU ======")
    print("1. View To-Do List")
    print("2. Add New Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. View Tasks by Day")
    print("6. Display Tasks Graph")
    print("7. Exit")
    print("============================")

def view_tasks(tasks):
    if len(tasks) == 0:
        print("\nNo tasks in the to-do list!")
    else:
        print("\nYour To-Do List:")
        for i, (task, date) in enumerate(tasks, start=1):
            print(f"{i}. {task} (Added on: {date})")

def add_task(tasks):
    task = input("\nEnter the new task: ")
    date = datetime.now().strftime("%Y-%m-%d")
    tasks.append((task, date))
    save_tasks_to_csv(tasks)
    print(f"Task '{task}' added on {date}!")

def update_task(tasks):
    if len(tasks) == 0:
        print("\nNo tasks to update!")
    else:
        view_tasks(tasks)
        task_num = int(input("\nEnter the task number to update: ")) - 1
        if 0 <= task_num < len(tasks):
            new_task = input("Enter the updated task: ")
            date = tasks[task_num][1]  # Keep the original date
            tasks[task_num] = (new_task, date)
            save_tasks_to_csv(tasks)
            print("Task updated!")
        else:
            print("Invalid task number!")

def delete_task(tasks):
    if len(tasks) == 0:
        print("\nNo tasks to delete!")
    else:
        view_tasks(tasks)
        task_num = int(input("\nEnter the task number to delete: ")) - 1
        if 0 <= task_num < len(tasks):
            removed_task = tasks.pop(task_num)
            save_tasks_to_csv(tasks)
            print(f"Task '{removed_task[0]}' deleted!")
        else:
            print("Invalid task number!")

def count_tasks_by_day(tasks):
    task_count = defaultdict(int)
    for _, date in tasks:
        task_count[date] += 1
    return task_count

def display_graph(task_count):
    dates = list(task_count.keys())
    counts = list(task_count.values())
    
    plt.figure(figsize=(10, 6))
    plt.bar(dates, counts, color='skyblue')
    plt.xlabel('Date')
    plt.ylabel('Number of Tasks')
    plt.title('Number of Tasks Added per Day')
    plt.xticks(rotation=45)
    plt.tight_layout()  # Adjust layout to make room for the rotated x-axis labels
    plt.show()

def main():
    tasks = load_tasks_from_csv()  # Load tasks from the CSV file
    
    while True:
        display_menu()
        choice = input("\nChoose an option (1-7): ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            task_count = count_tasks_by_day(tasks)
            display_graph(task_count)
        elif choice == '6':
            task_count = count_tasks_by_day(tasks)
            display_graph(task_count)
        elif choice == '7':
            print("Exiting the To-Do List program. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
