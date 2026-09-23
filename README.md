# TO-DO-LIST
The given project is a to do list management software.With the help of it, one can easily manage their tasks of a day,week or a month.

A simple command-line To-Do List manager written in Python. It lets you add, view, complete, and remove tasks through an interactive text menu.

Features
Add Task – Add a new task to your list.
View Tasks – Display all tasks along with their status (done / not done).
Mark Task as Done – Select a task by number and mark it as completed.
Remove Task – Select a task by number and delete it from the list.
Exit – Quit the application.
Requirements
Python 3.x (no external libraries required — uses only built-in functions)
Usage
When you run the program, you'll see a menu like this:
TO-DO LIST MENU
1.Add Task
2.View Tasks
3.Mark Task as Done
4.Remove Task
5.Exit

choose a number (1-5):
Enter a number from 1–5 to perform the corresponding action.

1. Add Task
Prompts you to type in a task description. The task is stored with a done status of False.
Enter the task: Buy groceries
Task added:Buy groceries

2. View Tasks
Lists all tasks with their index number and completion status.
Your Tasks:
1. Buy groceries : not done
2. Finish report : done
If no tasks exist, it prints:
No tasks yet!

3. Mark Task as Done
Shows the current task list, then asks for the task number to mark as complete.
Enter the task number to be marked as done: 1
Task 'Buy groceries' marked as done.
Handles invalid input (non-numeric entries or out-of-range numbers) gracefully.

4. Remove Task
Shows the current task list, then asks for the task number to delete.
Enter the task number that you want to remove:2
Removed task: Finish report
Also handles invalid input gracefully.

5. Exit
Prints Exit and terminates the program loop.

Data Structure
Tasks are stored in memory as a list of dictionaries:

python
tasks = [
    {"task": "Buy groceries", "done": False},
    {"task": "Finish report", "done": True}
]

