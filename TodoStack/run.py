import sqlite3
import Tkinter
from Tkinter import *
import tkMessageBox
#from task import Task, remove_task_from_database, cursor

# Starting connection to the database
connection = sqlite3.connect("store.db")
cursor = connection.cursor()


root = Tkinter.Tk()


# Creating table if not exists already
cursor.execute("CREATE TABLE IF NOT EXISTS Task(text TEXT, deadline TEXT, priority TEXT)")

def write_task_to_database(text, deadline, priority):
    cursor.execute("INSERT INTO Task (text, deadline, priority) VALUES(?, ?, ?)", (text, deadline, priority))
    connection.commit()

def fetch_tasks_from_database():
    cursor.execute("SELECT * FROM Task")
    tasks = cursor.fetchall()
    print "Fetching previous tasks from database"
    for text, deadline, priority in tasks:
        addTask2(text, deadline, priority)
    print "Done fetching,", len(tasks), "found"

def remove_task_from_database(text):
    print "Removing the task",
#    cursor.execute("SELECT * FROM Task")
    cursor.execute("""DELETE FROM Task WHERE text = "%s" """%text)
    connection.commit()
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
                remove_task_from_database(self.text)
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






# Setting up the header line
textHeader = Label(root, text="Text", width=40)
textHeader.grid(row=0, column=0)
deadlineHeader = Label(root, text="Deadline", width=20)
deadlineHeader.grid(row=0,column=1)
priorityHeader = Label(root, text="Priority", width=5)
priorityHeader.grid(row=0, column=2)

# Global variables go here
rows = 2
t, d, p = StringVar(), StringVar(), StringVar()

def addTask():
	global rows
	text = t.get().strip()
	deadline = d.get().strip()
	priority = p.get().strip()
        if not text or not deadline or not priority:
            remdata = ""
            if not text: remdata += "Text" + "\n"
            if not deadline: remdata += "Deadline" + "\n"
            if not priority: remdata += "Priority" + "\n"
            tkMessageBox.showerror("Error", "You need to fill the following to add task: \n" + remdata)
            return

	t.set("")
	d.set("")
	p.set("")
	newTask = Task(root, rows, text, deadline, priority)
	rows += 1
	newTask.configure()
        write_task_to_database(text, deadline, priority)


def addTask2(text, deadline, priority):
	#print "Task added: ", text, deadline, priority
        global root, rows
	newTask = Task(root, rows, text, deadline, priority)
	newTask.configure()
	rows += 1

# Adding entry fields
entryText = Entry(root, textvariable=t)
entryDeadLine = Entry(root, textvariable=d)
entryPriorityLevel = Entry(root, textvariable=p)
entryText.config(width=40)
entryDeadLine.config(width=20)
entryPriorityLevel.config(width=5)
entryText.grid(row=1, column=0)
entryDeadLine.grid(row=1, column=1)
entryPriorityLevel.grid(row=1, column=2)




# Configure submit button
submit = Button(root, command=addTask)
submit.config(text="add")
submit.grid(row=1,column=3)


fetch_tasks_from_database()

root.mainloop()

