from Tkinter import *

cursor = None
def remove_task_from_database(cursor, text):
    print "Removing the task",
    cursor.execute("SELECT * FROM Task")
    cursor.execute("DELETE FROM Task WHERE text = (?)", text)
    print "removed"

class Task:
        def __init__(self, root, row, text, deadline, priority):
                self.root = root
                self.row = row
                self.text = text
                self.deadline = deadline
                self.priority = priority
                self.removeButton = None
                print "New Task initialized"

        def remove(self):
                global remove_task_from_database
                self.entryText.grid_forget()
                self.entryDeadLine.grid_forget()
                self.entryPriorityLevel.grid_forget()
                self.removeButton.grid_forget()
                remove_task_from_database(cursor, self.text)
                print "Task with text:", self.text, "removed"

        def configure(self):
                self.entryText = Label(self.root, text=self.text)
                self.entryDeadLine = Label(self.root, text=self.deadline)
                self.entryPriorityLevel = Label(self.root, text=self.priority)
                self.removeButton = Button(self.root, text="remove", command=self.remove)

                self.entryText.config(width=40, bg='black', fg='lightgreen')
                self.entryDeadLine.config(width=20, bg='black', fg='lightgreen')
                self.entryPriorityLevel.config(width=5, bg='black', fg='lightgreen')

                self.entryText.grid(row=self.row, column=0)
                self.entryDeadLine.grid(row=self.row, column=1)
                self.entryPriorityLevel.grid(row=self.row, column=2)
                self.removeButton.grid(row=self.row, column=3)
                print "Newest task configured to fit in the window"


