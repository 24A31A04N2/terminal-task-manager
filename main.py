class Task:
    def __init__(self, title):
        self.title = title
        self.is_completed = False

    def mark_completed(self):
        self.is_completed = True

    def __str__(self):
        status = "[X]" if self.is_completed else "[ ]"
        return f"{status} {self.title}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        new_task = Task(title)
        self.tasks.append(new_task)
        print(f"Task '{title}' added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available. Em panulu levu!")
            return
        print("\n--- Your Tasks ---")
        for index, task in enumerate(self.tasks):
            print(f"{index + 1}. {task}")
        print("------------------\n")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
            print("Task marked as completed!")
        else:
            print("Invalid task number.")


# Main Program Loop (Terminal Interface)
def main():
    manager = TaskManager()
    
    while True:
        print("\n1. Add Task  2. View Tasks  3. Complete Task  4. Exit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            title = input("Enter task name: ")
            manager.add_task(title)
        elif choice == '2':
            manager.view_tasks()
        elif choice == '3':
            manager.view_tasks()
            try:
                task_num = int(input("Enter task number to complete: ")) - 1
                manager.complete_task(task_num)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            print("Goodbye! Bye bye!")
            break
        else:
            print("Invalid choice. Malli try cheyandi.")

if __name__ == "__main__":
    main()