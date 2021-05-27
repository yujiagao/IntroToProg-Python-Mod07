**Gao Yujia**

*23 May 2021*

*Foundations of Programming: Python*

*Assignment07*


***Files and Exception***

Introduction:
This module talks about the use of binary files and exceptions. Binary files, as mentioned in the tutorial, are not encrypted files, but are files that have a certain level of security in them. In order to read or write binary files, we need to use the ‘pickle’ function of Python in order to make sense of the data. 
‘Try and Except’ are a way for us to deal with the inconsistent and variable way users input data into the script. Instead of crashing the whole script with an incorrect input, ‘Try and Except’ is an automated way for the script to try and correct for this errors by prompting the users where their error is. We  can either use a pre-existing library of exceptions, or if we are adventurous enough we can create custom exceptions as well. 

Creating the Python File
In this assignment, I have decided to include a little bit of everything I’ve learnt so far. This starts with creating the log, and importing the ‘pickle’ function
```
# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Pickle and Exceptions
# ChangeLog (Who,When,What):
# GYJ, 22.5.21, Creation of Assignment 07 file
# GYJ, 24.5.21 ,Addition of code to complete Assignment 07
# ---------------------------------------------------------------------------- #

import pickle

#--Data--#
strTask = ""                         # string task to include in table
strPriority = ""                     # priority of task
lstTable = []                        # table list
file_name = "picklelist.dat"         # .dat file to save into
choice = ""                          #menu selection
```
I next created a set of functions which I will use for the processing part of the script (Fig. 2)

```
#-- Processing --#

def write_to_file(data, file_name):
    """ Creates binary file and writes to file"""
    objfile = open(file_name, 'ab')     #opens a binary file
    pickle.dump(data, objfile)          #writes pickle data to file
    objfile.close

def add_data_to_list(task, priority, list_of_rows):    #adds data to the file
    dicRow = {"Task": task, "Priority": priority}      #creates a dictionary
    list_of_rows.append(dicRow)
    return list_of_rows, 'Success'

def remove_data_from_list(task, list_of_rows):         #removes data from the file
    for row in list_of_rows:
        if row["Task"].lower() == task.lower():
                list_of_rows.remove(row)
                print("Task Removed")
                break
        else:
                print("Task not found")                #prompt to user if they made an invalid entry
    return list_of_rows, 'Success'

def read_from_file(file_name):                         #unpickle a file
    """read pickle data from file"""
    objfile = open(file_name, 'rb')
    data = pickle.load(objfile)
    return data

def print_menu():
    print('''
    Menu of Options
    1) Add a new Task
    2) Remove an existing Task
    3) Save Data to File        
    4) Read Data from File
    5) Exit Program
    ''')
    print()  # Add an extra line for looks

def menu_choice():
    try:                                                       #this part will run if the user puts a correct  entry
        choice = int(input("Please Enter Your Option:  "))
        print()
        return choice
    except ValueError:                                         #if a wrong entry is made, a prompt is given
        print("Please choose an option from 1 to 5")

```
Once this is done, I created the main script. Instead of creating functions for the input and output part, I kept them as individual scripts (Fig. 3)
 
```
#-- Main script --#

while(True):
    print_menu()
    choice = menu_choice()

    if choice == 1:
        strTask = input(str("Please Enter New Task:  "))                #task to input
        strPriority = input(str("Please Enter Priority of Task:  "))    #priority to input
        data = add_data_to_list(strTask, strPriority, lstTable)
        print(data)
        input('Press the [Enter] key to continue.')
        continue
    elif choice == 2:
        strTask = input(str("Please Enter Task to Remove:  "))          #task to remove
        data = remove_data_from_list(strTask, lstTable)
        print(data)
        input('Press the [Enter] key to continue.')
        continue
    elif choice == 3:
        write_to_file(data, file_name)                                  #write to a binary file
        print("Data saved")
        input('Press the [Enter] key to continue.')
        continue
    elif choice == 4:                                                   #read from the binary file
        data = read_from_file(file_name)
        print(data)
        input('Press the [Enter] key to continue.')
        continue
    elif choice == 5:
        print("Goodbye!")
        break
```

When the script is run, the first part of entering data into the table is straightforward (Fig. 4)
 
![Fig. 4](https://github.com/yujiagao/IntroToProg-Python-Mod07/blob/main/Picture4.png "Fig. 4")

Next is removing data from the table (Fig. 5)
 
![Fig. 5](https://github.com/yujiagao/IntroToProg-Python-Mod07/blob/main/Picture5.png "Fig. 5")

In order to test the try-except part of the code, I deliberately entered a string input when the code is expecting an integer input, resulting in the except error message being displayed ((Fig. 6)
 
![Fig. 6](https://github.com/yujiagao/IntroToProg-Python-Mod07/blob/main/Picture6.png "Fig. 6")

Saving the data using pickle and subsequently unpickling it is also performed (Fig. 7)
 
![Fig. 7](https://github.com/yujiagao/IntroToProg-Python-Mod07/blob/main/Picture7.png "Fig. 7")

As this data was saved as a binary file using the pickle function, it appears very differently compared to a standard .txt file (Fig. 8)
 
![Fig. 8](https://github.com/yujiagao/IntroToProg-Python-Mod07/blob/main/Picture8.png "Fig. 8")

Conclusion:
Exceptions allow us to cater for user input errors without it crashing the entire script. It is extremely useful as there is already an existing library of standard exception messages, depending on what error is received. The ability to customise those messages are also a plus point and sometimes the standard messages may not always communicate what we want. 
Saving in binary may seem as an unnecessary step, however sometimes we do want to add an extra layer of security to our files, without having to encrypt it. This is an extremely useful function and will serve well to provide some level of protection to our data.
