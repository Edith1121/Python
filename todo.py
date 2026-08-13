import json 
import os


os.chdir("CLI_to_do_list")

try:
     with open("tasks.json", "r") as file:
        tasks = json.load(file)

except FileNotFoundError:
     tasks = []
     print("\ntasks.json not found. Starting with an empty task list.")

except json.JSONDecodeError:
     print("\ntasks.json contains invalid JSON.")
     tasks = []

def home_page():
    while True:
        print("------TO-DO LIST-------")
        try:
            user_need = int(input(""" What do you want to do ?
    1.View Tasks
    2.Add Tasks
    3.Delete Task
    4.Modify
    5.EXIT
                
    Please enter the number of your selection : """))
        except ValueError:
                print("\nPlease enter a number!")
                continue

      
        if user_need == 1:
            view_tasks(tasks)

        elif user_need == 2:
            add_tasks()
            
        elif user_need == 3:
            dlt_tasks()

        elif user_need == 4:
             modify_task()

        elif user_need == 5:
            print("Goodbye!")
            return
        else:
            print("\nInvalid Option Selected!")

def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)
        

def view_tasks(tasks):
    for num,i in enumerate(tasks,start=1):
        print(f'{num}.{i["task"]} : [{" " if i["completed"] is  False else "✓"}]')

    input("\nPress Enter to return to the home page...")
    return
                    


def add_tasks():
    running = True
    while running:
        adding_task = input("\nEnter the task to be added : ").strip()

        if not adding_task:
             print("Please enter a taskname!")
             continue
        tasks.append(
            {
            "task" : adding_task,
            "completed" : False
            }
        )

        save_tasks()

        print(f"\nSuccesfully added {adding_task}")
        
        try:
          next_task = int(input("""
1.Add another task
2.Go to Home page
3.View Tasks
Select your option : """))
        except ValueError:
             print("\nPlease enter a number!")
             continue
        
        if next_task == 1:
            continue
        elif next_task == 2:
            return
        elif next_task == 3:
            view_tasks(tasks)
            return
        else:
            print("\nInvalid option number!")
    return

def dlt_tasks():
     if not tasks:
        print("\nThere are no tasks to delete.")
        input("Press Enter to return to the home page...")
        return
     
     while True:
        for num, i in enumerate(tasks,start=1):
            print(f'{num}.{i['task']} : [ {"✓" if i["completed"] else " "}]')

        try:
         choice = int(input("\nEnter the number of the task which you need to delete : "))

        except ValueError:
             print("\nPlease enter a number!")
             continue
        
        if 1<= choice <= len(tasks):
            tasks.pop(choice -1)

            save_tasks()

            print("Task deleted")

            for num, i in enumerate(tasks,start=1):
                        print(f'{num}.{i['task']} : [ {"✓" if i["completed"] else " "}]')

        else:
             print("\nInvalid task number")
             continue
        try:
         response = int(input("""
1.Delete another task
2.Go to home page
Select your option : """))
        except ValueError:
            print("\nPlease enter a number!")
            continue

        if len(tasks) > 0 and response == 1:
                continue
        elif response == 2:
            return
        else:
            return

def modify_task():
     if not tasks:
        print("\nThere are no tasks to modify.")
        input("Press Enter to return to the home page...")
        return

     for num, i in enumerate(tasks,start=1):
                 print(f'{num}.{i['task']} : [ {"✓" if i["completed"] else " "}]')
     try:
      usr_choice = int(input("\nEnter the number of task to be modified : "))

     except ValueError:
      print("Please enter a number!")
      return

     if not (1 <= usr_choice <= len(tasks)):
         print("Invalid task number")
         return

     while True:
          
          name_or_status = input("""
What do you want to modify taskname(n) or status(s),
Enter the respective character (n/s) : """).lower()
          
         

          if name_or_status == "n":
                new_name = input("\nEnter the new name for the selected task : ").strip()

                if not new_name:
                     print("\nTask name cannot be empty")
                     continue
                
                tasks[usr_choice-1]["task"] = new_name
                print("\nModifications done :)")
                save_tasks()
                return

          elif name_or_status == "s":
                while True:
                    completed_or_not = input("\nDid you complete that task (y/n)? : ").lower()
                    
                    if completed_or_not == "y":
                            tasks[usr_choice-1]["completed"] = True

                            save_tasks()
                            print("\nModifications done :)")
                            return
                    
                    elif completed_or_not == "n":
                            tasks[usr_choice-1]["completed"] = False
                            save_tasks()
                            print("\nModifications done :)")
                            return
                    
                    else:
                        print("\nPlease enter a valid option!")
                        continue

          else:
                 print("\nInvalid option selected!")
     

home_page()