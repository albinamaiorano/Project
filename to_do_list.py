import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('todo.db')
c = conn.cursor()

# Create tasks table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS tasks (
             id INTEGER PRIMARY KEY,
             task TEXT NOT NULL,
             completed INTEGER DEFAULT 0
             )''')

# Function to add a task
def add_task(task):
    c.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
    conn.commit()
    print("Task added successfully!")

# Function to mark a task as completed
def complete_task(task_id):
    c.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
    conn.commit()
    print("Task marked as completed!")

# Function to delete a task
def delete_task(task_id):
    c.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    print("Task deleted successfully!")

# Function to view tasks
def view_tasks():
    c.execute("SELECT * FROM tasks")
    tasks = c.fetchall()
    if not tasks:
        print("No tasks found.")
    else:
        for task in tasks:
            status = "Completed" if task[2] == 1 else "Not Completed"
            print(f"{task[0]}. {task[1]} - {status}")

# Main function
def main():
    while True:
        print("\nTodo List Application")
        print("1. Add Task")
        print("2. Complete Task")
        print("3. Delete Task")
        print("4. View Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '2':
            task_id = int(input("Enter the task ID to mark as completed: "))
            complete_task(task_id)
        elif choice == '3':
            task_id_input = input("Enter the task ID to delete: ")
            try:
                task_id = int(task_id_input)
                delete_task(task_id)
            except ValueError:
                print("Invalid task ID. Please enter a valid integer.")
        elif choice == '4':
            view_tasks()
        elif choice == '5':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()

# Close database connection
conn.close()
