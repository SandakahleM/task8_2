#=====importing libraries===========
'''This is the section where you will import libraries'''
from datetime import datetime,date

#====Login Section====
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file.
    - Use a while loop to validate your user name and password.
'''
logins = []
with open("user.txt", "r") as f:
    for line in f.readlines():
        user, passw = line.split(", ")
        logins.append((user.strip(), passw.strip()))
#print(logins)
#
while True:
  username = input("Enter your Username :")
  password = input("Enter your Password :")
  if (username, password) in logins:
        print("Welcome")
        break
  else:
    print("Incorrect username or password", "Please try again", sep='\n')     
    continue
  
while True:
    #presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower()

    if menu == 'r':
        pass
        '''In this block you will write code to add a new user to the user.txt file
        - You can follow the following steps:
            - Request input of a new username
            - Request input of a new password
            - Request input of password confirmation.
            - Check if the new password and confirmed password are the same.
            - If they are the same, add them to the user.txt file,
            - Otherwise you present a relevant message.'''
        new_username = input("Enter your Username :")
        new_password = input("Enter your Password :") 
        if username != "admin":
            print("You are not allawed to register users")

        elif username == "admin":
         file = open("user.txt","a")
         file.write("\n")
         file.write(new_username)
         file.write(", ")
         file.write(new_password)
         file.write("\n")
         file.close()
         print("Username " + new_username + " has been created " )

    elif menu == 'a':
        pass
        '''In this block you will put code that will allow a user to add a new task to task.txt file
        - You can follow these steps:
            - Prompt a user for the following: 
                - A username of the person whom the task is assigned to,
                - A title of a task,
                - A description of the task and 
                - the due date of the task.
            - Then get the current date.
            - Add the data to the file task.txt and
            - You must remember to include the 'No' to indicate if the task is complete.'''
      

        username = input("Enter your Username of the person the task is assigned to :")
        title_of_the_task= (input("Enter your job title: "))
        description=input("Enter job discription: ")
        current_date = date.today()
        day = int(input('Enter a day for due date: '))
        month =input('Enter a month for due date : ')
        year = int(input('Enter a year for due date : '))
        due_date = year, month, day
        
        file = open("tasks.txt","a")
        file.write("\n")
        file.write(username +", " + title_of_the_task + ", " + 
                   description + ", " + str(current_date) + ", " + str(due_date) +", No" )
        
        file.close()
        print("Task " + title_of_the_task + " has been created " )

    elif menu == 'va':
        pass
        '''In this block you will put code so that the program will read the task from task.txt file and
         print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
         You can do it in this way:
            - Read a line from the file.
            - Split that line where there is comma and space.
            - Then print the results in the format shown in the Output 2 
            - It is much easier to read a file using a for loop.'''
        file = open("tasks.txt","r")
        print(file.read())
        file.close()

    elif menu == 'vm':
        pass
        '''In this block you will put code the that will read the task from task.txt file and
         print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
         You can do it in this way:
            - Read a line from the file
            - Split the line where there is comma and space.
            - Check if the username of the person logged in is the same as the username you have
            read from the file.
            - If they are the same print it in the format of Output 2 in the task PDF'''
        tasks = []
        with open("tasks.txt", "r") as f:
         for user_task in f:
          users = user_task.strip()
          users = user_task.split(", ")
          tasks.append(user_task[:0])
        
        print(tasks)
              
    elif menu == 'e':
        print('Goodbye!!!')
        exit()


    else:
        print("You have made a wrong choice, Please Try again")


"""  

    
    

    else:
        print("You have made a wrong choice, Please Try again") """