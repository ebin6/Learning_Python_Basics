tasks={

}
id=1

def AddTask(task):
    global tasks
    global id
    tasks[id]={"tasks":task,"status":False}
    id+=1

def UpdateTask(task_id):
    global tasks
    my_task=tasks.get(task_id)

def RemoveTask(id):
    pass

def ShowTask():
    print(tasks)

while True:
    print("ToDo Tasks")
    print("1.Add Task\n2.Update Task\n3.Remove Task\n4.Show Task")
    choice=int(input("Enter your choice : "))
    match choice:
        case 1:
            task=input("Enter the task : ")
            AddTask(task)
        case 2:
            task_id=int(input("Enter the task id : "))
            UpdateTask(task_id)
        case 3:
            task_id = int(input("Enter the task id : "))
            RemoveTask(task_id)
        case 4:
            ShowTask()
        case __:
            print("Please enter valid choice")