tasks = []
def add_task():
    """
    Adding Tasks to the list
    """
    
    """
    Addding no. of tasks into a list i.e tasks[]
    """
    #Opening the txt file & writing to it 
    #file = open('D:\Future\Python Technical Director\Git', 'w')
    
    n_tasks = 2
    for i in range(n_tasks):

        task = input("\nEnter a new task: ")     

        tasks.append({"task": task, "Complete": False})
        #file.write(str(tasks))
        print("Task succecefully added!")

        

    #file.close()#Closing file to save the content 
    
    """
    15 min Counting down for all tasks to be submitted
    """

    
def view_task():

    """
    View tasks from the list
    Checks if any task is added
    """
    # checks if the are no tasks added! else add no. of tasks
    if len(tasks) == 0:

        print("No tasks added.")
    else:
        print('list of tasks :')
        for i, task in enumerate(tasks):
            status = "Complete" if task["Complete"] else "Not Complete"
            print(f'{i + 1} . {task['task']} - {status}')

  
  
def main():
    #Main menu of the Application
    while True:
        print("\n************ To-Do List Application ***************")
        print("1. Add tasks")
        print("2. View tasks")
        

        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_task()
           
        elif choice == 2:
           view_task()  
        elif choice == 3:
            break
        else:
            print('Invalid choice. Please try again! ')


#if "__name__" == "__main__":
main()


