myTasks = {}

while True:
    taskname = raw_input("Enter taskName, or 'x' to finish: ")

    if taskname == 'x':
        break

    completed = raw_input("Task is completed? (y,n)")

    isCompleted = True if completed == 'y' else False
    myTasks[taskname] = isCompleted

print myTasks

