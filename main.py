import sqlite3
from datetime import datetime


def create_connection():
    return sqlite3.connect("tasks.db")


def create_table():
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        created_at TEXT
    )
    """)

    connection.commit()
    connection.close()


def add_task():
    title = input("Task title: ")
    description = input("Task description: ")
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M")

    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO tasks (title, description, created_at) VALUES (?, ?, ?)",
        (title, description, created_at)
    )

    connection.commit()
    connection.close()

    print("Task added successfully.")


def list_tasks():
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()

    connection.close()

    if not tasks:
        print("No tasks found.")
        return

    print("\n--- TASK LIST ---")
    for task in tasks:
        print(f"ID: {task[0]}")
        print(f"Title: {task[1]}")
        print(f"Description: {task[2]}")
        print(f"Created at: {task[3]}")
        print("-" * 20)


def delete_task():
    task_id = input("Enter task ID to delete: ")

    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    connection.commit()
    connection.close()

    print("Task deleted (if ID existed).")


def update_task():
    task_id = input("Enter task ID to update: ")
    new_title = input("New title: ")
    new_description = input("New description: ")

    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE tasks
        SET title = ?, description = ?
        WHERE id = ?
    """, (new_title, new_description, task_id))

    connection.commit()
    connection.close()

    print("Task updated (if ID existed).")


def menu():
    while True:
        print("\n--- TASK MANAGER ---")
        print("1. Add task")
        print("2. List tasks")
        print("3. Update task")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid option.")


create_table()
menu()


