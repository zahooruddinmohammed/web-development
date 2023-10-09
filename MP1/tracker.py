from datetime import datetime
import json
import os

tasks = []
# constant, don't edit, use .copy()
TASK_TEMPLATE = {
    "name":"",
    "due": None, # datetime
    "lastActivity": None, # datetime
    "description": "",
    "done": False # False if not done, datetime otherise
}

# don't edit, intentionaly left an unhandled exception possibility
def str_to_datetime(datetime_str):
    """ attempts to convert a string in one of two formats to a datetime
    Valid formats (visual representation): mm/dd/yy hh:mm:ss or yyyy-mm-dd hh:mm:ss """
    try:
        return datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S')
    except:
        return datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')

def save():
    """ writes the tasks list to a json file to persist changes """
    f = open("tracker.json", "w")
    f.write(json.dumps(tasks, indent=4, default=str))
    f.close()

def load():
    """ loads the task list from a json file """
    if not os.path.isfile("tracker.json"):
        return
    f = open("tracker.json", "r")
    
    data = json.load(f)
    # Note about global keyword: https://stackoverflow.com/a/11867510
    global tasks
    tasks = data
    f.close()
    print(f"data {data}")    

def list_tasks(_tasks):
    """ List a summary view of all tasks """
    i = 0
    for t in _tasks:
        print(f"{i+1}) [{'x' if t['done'] else ' '}] Task: {t['name']} (Due: {t['due']})")
        i += 1
    if len(_tasks) == 0:
        print("No tasks to show")

# edits should happen below this line

def add_task(name: str, description: str, due: str):
    """ Copies the TASK_TEMPLATE and fills in the passed in data then adds the task to the tasks list """
    task = TASK_TEMPLATE.copy()            # don't delete this; use this task reference for the below requirements
    now= datetime.now()                    #update lastActivity with the current datetime value
    dt_string=now.strftime("%m%d%y %H:%M:%S")
    if name=="":                           #validating for input name,description and due
        print("task failed,please enter valid name")
        return
    elif description=="":
        print("task failed,please enter valid description")
        return
    elif due=="":
        print("task failed,please enter valud due date")
        return 
    try:    
        str_to_datetime(due)                # due date must match one of the formats mentioned in str_to_datetime()
    except Exception as e:
        print("Invalid due date format. Use 'mm/dd/yy hh:mm:ss' or 'yyyy-mm-dd hh:mm:ss'")
        return
    task['name']=name                       #set time
    task['due']= due                        #set due
    task['description']=description         #set description
    task['lastActivity']=dt_string          #set last activity with current datetime value
    task["done"]= False                     #false if not done,dattime otherwise
    tasks.append(task)                      #add the new task to the tasks list
    print("task added successfully.")       #output a message confirming the new task was added or if the addition was rejected due to missing data based on the prior checks
    #summary: with the help of copy function from copy module to the task dic and initialuzed it with values from the user input.
    # and wit the user input appended it to the task list.
    #zm254-10/05/2023
    save()                                  #make sure save() is still called last in this function
   
def process_update(index):
    """ extracted the user input prompts to get task data then passes it to update_task() """
    # get the task by index - task[index]
    if len(tasks)-1 < index or index < 0:   #consider index out of bounds scenarios and include appropriate message(s) for invalid index
        print(f"index out of bounds,please enter a index less than or equal to {len(tasks)} and greater than zero")
        return
    # show the existing value of each property where the TODOs are marked in the text of the inputs below (replace the TODO related text with the found tasks's data)
    #summary:To start i passed index to task list to et the index number,later to the same i passed name,description
    #and due to get the current name,description and due of the input index by the user.
    #zm254-06/10/2023
    name = input(f"What's the name of this task? Curent name: {tasks[index]['name']} \n").strip()
    desc = input(f"What's a brief descriptions of this task?Curent description: {tasks[index]['description']}\n").strip()
    due = input(f"When is this task due (format: m/d/y H:M:S) Curent due: {tasks[index]['due']} \n").strip()
    update_task(index, name=name, description=desc, due=due)

def update_task(index: int, name: str, description:str, due: str):
    """ Updates the name, description , due date of a task found by index if an update to the property was provided """
    #zm254-10/06/23
    #summary: To start with i did the validation for index out of bound scenario by writing a if condition and 
    #checking if the length of tasks-1 is less than index
    #or index is less than zero if this condition is true then the index is outof bound,
    #i will be displaying an error message for the same.
    #later calling 3 if condition for name description and due to check if it not equal to a empty string,
    #if the condition passes then i will be takingthe input
    #passed from the process_update function and replacing with the existing values.
    #by using datetime class from datetime module i am taking current time in mm/dd/yy H:M:S format and
    #overiding the current lastactivity value.
    #for the final output for success message i am using a variable is_updated which will be initially false,
    #which i will be makingtrue if a if condition is executed
    #In the end if the is_updated is true then i am printing the success message else i will print the task not updated message.
                                                    #find the task by index -tasks[index]
    is_updated= False
    if(len(tasks)-1)< index or index< 0:            #consider index out of bounds scenarios and include appropriate message(s) for invalid index
        print(f"index out of bounds,please enter a index less than or equal to {len(tasks)} and greater than 0")
        return
    if description!= "":
        tasks[index]['description']=description     #update incoming task data if it's provided (if it's not provided use the original task property value)
        is_updated=True
    if name!= "":
        tasks[index]['name']=name                   #update incoming task data if it's provided (if it's not provided use the original task property value)
        is_updated=True
    if due!= "":
        tasks[index]['due']=due                     #update incoming task data if it's provided (if it's not provided use the original task property value)
        is_updated=True 
    now= datetime.now()                             #datettime object containing current date and time
    dt_String= now.strftime("%m%d%y %H:%M:%S") 
    tasks[index]['lastActivity']=dt_String          #update lastActivity with the current datetime value
    if is_updated:
        print("task successfully updated")          #output that the task was updated if any items were changed, otherwise mention task was not updated
    else:
        print("task was not updated there were no changes made")
    save()                                          #make sure save() is still called last in this function

def mark_done(index):
    """ Updates a single task, via index, to a done datetime"""
                                                    #find task from list by index- tasks[index]
    if len(tasks)-1 < index or index<0:             #consider index out of bounds scenarios and include appropriate message(s) for invalid index
        print(f"index out of bounds,please enter a index less or equal to {len(tasks)}and greater than 0")
        return
    if tasks[index]['done']==False:                 #if it's not currently marked as done, record the current datetime as the value (don't just set it as true)
        tasks[index]['done'] = True
        now=datetime.now()                          #datetime object containing current date and time
        dt_string = now.strftime("%m%d%y %H:%M:%S") #mm/dd/yy H:M:s
        tasks[index]['lastActivity']=dt_string      #if its not done,record the current datetime as the value
        print("task was marked done successfully")  #if its done, print a message saying its already completed
    else:
        print("task is already completed")          #if it is currently done, print a message saying it's already been completed
    
    #summary:checking for the index out of bounds scenarios like the usual way like how i have done in the previous functions.
    #for the main function i am using a if else condition in which i am checking if done is equal to true for the given index,
    #if the condition passes then i am marketing done as true and
    #updating the lastActivity to current datetime by using the datetime class fromdatetime module and formatting the datetime
    #acc to our format req format and t am also printing the task was done successfully message.
    #in the else i am printing the message task is already completed.
    #zm254-10/06/2023
    save()                                          #make sure save() is still called last in this function

def view_task(index):
    """ View more info about a specific task fetch by index """
                                                    #find task from list by index - tasjs[index]
    if len(tasks)-1 < index or index<0:             #consider index out of bounds scenarios and include appropriate message(s) for invalid index
        print(f"index out of bounds,please enter a index less or equal to {len(tasks)}and greater than 0")
        return
    task = {                                        #<-- replace or update the assignment of this variable, I just used an empty dict so it would run without changes
        "name":tasks[index]['name'],
        "due": tasks[index]['due'],
        "lastActivity":tasks[index]['lastActivity'],
        "description":tasks[index]['description'],
        "done": tasks[index]['done']
    }
                                                    #utilize the given print statement when a task is found
    print(f"""
          [{'x'if task['done']else ''}]
          task: {task['name']}\n
          Description: {task['description']}\n
          Last Activity: {task['lastActivity']}\n
          Due: {task['due']}\n
          Complete: {task['done']if task['done']else '-'}\n
        """.replace(' ',' '))
    #zm254-10/06/2023
    #summary:To start with checking the index out of bound scenarios in the usual way(like prev func)
    #to the empty dict task i passed key of name,due,lastactivity, description, done and their value using index.
    #using this dict task we are printing the request for view function


def delete_task(index):
    """ deletes a task from the tasks list by index """
                                                    #delete/remove task from list by index
                                                    #message should show if it was successful or not
    if len(tasks)-1 < index or index<0:             #consider index out of bounds scenarios and include appropriate message(s) for invalid index
        print(f"index out of bounds,please enter a index less or equal to {len(tasks)}and greater than 0")
        return
    tasks.remove(tasks[index])
    print("task deleted successfully")
    #zm254-10/06/2023
    #summary:To start with i am checking the index out of bound senarios in the usual was(like previous functions)
    #to remove a particular task i am using remove() method
    #- the remove() method takes a single element as an argument and removes it from the list.
    #in the end printing for calling the save() function and
    #printing  a success message if the task is deleted successfully.
    save()                                          #make sure save() is still called last in this function

def get_incomplete_tasks():
    """ prints a list of tasks that are not done """
    #zm254-10/06/23
    #summary:
    #in the for loop we can check a condition if any task isnt having ant task['done']= true
    #then we are appendinf those tasking to the empty list
    #which is _tasks = [] which is predeclared in template.
    #list is being passed to list_task functions where the print stmt iscalled for this.
    _tasks = []
    
    for task in tasks:
        if task['done'] == False:
            _tasks.append(task)                     # <-- this is a placeholder to populate based on the above requirements
    list_tasks(_tasks)                              # pass that list into list_tasks()

def get_overdue_tasks():
    """ prints a list of tasks that are over due completion (not done and expired) """
    #zm254-10/06/2023
    #summary: using datetime class from datetime module for compating with the due time to checking if the task is overdue ornot.
    #appending those tasks which satisfy the if condtion to emplty list of _tasks.
    #overdue data in my list _tasks, which i am passing to list_taks.
    #list_taks function has a print stmt which is printing the result for this function
    now= datetime.now()                                                 #datetime object containting current date and time
    _tasks = []                                                       #<-- this is a placeholder to populate based on the above requirements
    for task in tasks:
        if task['done']== False and str_to_datetime(task['due'])<now:   #generate a list of tasks where the due date is older than "now" and that are not complete (i.e., not done)
             _tasks.append(task)                                        #pass that list into list_tasks()
    list_tasks(_tasks)

def get_time_remaining(index):
    """ outputs the number of days, hours, minutes, seconds a task has before it's overdue otherwise shows similar info for how far past due it is """
    #zm254-10/06/23
    #summary:in the start checking the index out of bond scenarios in the usual way as was done before
    #using datetime class from datetime module to get current date and time
    #for this funcrion i have 3 conditional stmts
    #for the first if conditon there are two condtions 
    #which for the first is done is equal to false  and later the due date of the task for the given index is <=current time.
    #if this passes an print stmt is passed statingthe remaining time by sub the due date by curr time
    #2ifelse condtion same logic having 2 condition but int he later checking 
    #the due date of the tast for the fien index is >= curren time
    #creating new variable to store due time and also creating remaining time to subtract from due time to current time
    #if both above if else fails then the last is executed, meaning task is completed
    now=datetime.now()#datetime object containing current date and time.
    task=tasks[index] #get the task by index -task[index]
    if len(tasks)-1 < index or index<0:                                 #consider index out of bounds scenarios and include appropriate message(s) for invalid index
        print(f"index out of bounds,please enter a index less or equal to {len(tasks)}and greater than 0")
        return                                                          #get the days, hours, minutes, seconds between the due date and now
                                                                        # display the remaining time via print in a clear format showing X days, X hours, X minutes, X seconds (time components must be clearly separated)
    if tasks[index]['done']==False and str_to_datetime(tasks[index]['due'])>=now:
        due_date = str_to_datetime(tasks[index]['due'])
        remaining_time = due_date - now
        print(f"the remaining time for this task is {remaining_time}")
                                                                        # if the due date is in the past print out how many days, hours, minutes, seconds the task is overdue (clearly note that it's overdue, values should be positive)
    elif tasks[index]['done']== False and str_to_datetime(tasks[index]['due'])<now:
        print(f"the task is overdue by {now - str_to_datetime(tasks[index]['due'])}")
    else:
        print("the task is already completed")

    
# no changes needed below this line

command_list = ["add", "view", "update", "list", "incomplete", "overdue", "delete", "remaining", "help", "quit", "exit", "done"]
def print_options():
    """ prints a readable list of commands that can be typed when prompted """
    print("Choices")
    print("add - Creates a task")
    print("update - updates a specific task")
    print("view - see more info about a task by number")
    print("list - lists tasks")
    print("incomplete - lists incomplete tasks")
    print("overdue - lists overdue tasks")
    print("delete - deletes a task by number")
    print("remaining - gets the remaining time of a task by number")
    print("done - marks a task complete by number")
    print("quit or exit - terminates the program")
    print("help - shows this list again")

def run():
    """ runs the program until terminated or a quit/exit command is used """
    print("Welcome to Task Tracker!")
    load()
    print_options()
    while(True):
        opt = input("What would you like to do?\n").strip() # strip removes whitespace from beginning/end
        if opt not in command_list:
            print("That's not a valid option")
        elif opt == "add":
            name = input("What's the name of this task?\n").strip()
            desc = input("What's a brief descriptions of this task?\n").strip()
            due = input("When is this task due (visual format: mm/dd/yy hh:mm:ss)\n").strip()
            add_task(name, desc, due)
        elif opt == "view":
            num = int(input("Which task do you want to view? (hint: number from 'list') ").strip())
            index = num-1
            view_task(index)
        elif opt == "update":
            num = int(input("Which task do you want to update? (hint: number from 'list') ").strip())
            index = num-1
            process_update(index)
        elif opt == "done":
            num = int(input("Which task do you want to complete? (hint: number from 'list') ").strip())
            index = num-1
            mark_done(index)
        elif opt == "list":
            list_tasks(tasks)
        elif opt == "incomplete":
            get_incomplete_tasks()
        elif opt == "overdue":
            get_overdue_tasks()
        elif opt == "delete":
            num = int(input("Which task do you want to delete? (hint: number from 'list') ").strip())
            index = num-1
            delete_task(index)
        elif opt == "remaining":
            num = int(input("Which task do you like to get the duration for? (hint: number from 'list') ").strip())
            index = num-1
            get_time_remaining(index)
        elif opt in ["quit", "exit"]:
            print("Good bye.")
            quit()
        elif opt == "help":
            print_options()
        
if __name__ == "__main__":
    run()