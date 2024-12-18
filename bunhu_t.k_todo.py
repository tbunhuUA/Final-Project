import argparse
import os

#This program allows the user to manage a single todo list or multiple lists

#This checks to if is the default todo list exists; if not, one is made
if os.path.exists('TODO.txt'):
    pass
else:
    with open('TODO.txt', 'w') as todo:
        pass

# Create the parser
parser = argparse.ArgumentParser(description="Manages todo list(s)")

#The various arguments of the program to be added
parser.add_argument('-l', '--list', help='Specifies which todo list the program works with; if not specified, the program writes to the default todo list')
parser.add_argument('-d', '--display', type=int, help='Displays all the items of the todo list; input 1 to use')
parser.add_argument('-i', '--id', type=int, help='An input item used to call a specific value by the id')
parser.add_argument('-a', '--add', type=int, help='Adds a new item to the todo list; input 1 to use')
parser.add_argument('-s', '--status', help='Changes the status of an item; done by a single character (or typing out the whole thing): p for In-Progress, i for Incomplete, c for Complete; Specify the item to be change by using --id')
parser.add_argument('-u', '--update', type=int, help='Used to change either the (1)Category or (2)Description; specific by inputting the associated numerical value; specify the item to be change by using --id')


# Parse arguments
args = parser.parse_args()

#There are 4 components of a todo item: ID, Category, Description, and Status
#Each component is represented by an individual list in the program
#Positioning matters heavily because the every component of a single item has to share the same index
id = [] #1: ID is counted starting from 1, in an order of when an item was added
idCount = 0 #Used to note how many items there are, needed to add a new id for a new item
category = [] #2: The type of item; limited to ten characters
description = [] #3: What the item is; must be greater than ten characters
status = [] #4: the state of the item; can be only either incomplete (i in the file), in progress (p in the file), or complete (c in the file)

#Here's how each item looks in the file
#id (example: 1)
#status (example: p)
#category (example: Category1)
#description (example: Description1)

#This is what breaks down the information in the files into their respective lists
#It checks which list is being used which is defined by the user, the default list is used if undefined
if args.list == None:

    file = 'TODO.txt'

    with open(file, 'r') as todo:
        for line in todo:
            line = line.strip()
            #Checks for the only numerical value ID
            try:
                value = int(line) 
            except ValueError:
                if line == 'p' or line == 'i' or line == 'c':
                    if line == 'p':
                        status.append('In-Progress')
                    elif line == 'i':
                        status.append('Incomplete')
                    elif line == 'c':
                        status.append('Complete')
                elif len(line) <= 10:
                    category.append(line)
                elif len(line) > 10:
                    description.append(line)
            else:
                id.append(value)
                idCount = idCount + 1
else:
    file = args.list + ".txt"

    if os.path.exists(file):
        pass
    else:
        with open(file, 'w') as todo:
            pass

    with open(file, 'r') as todo:
        with open(file, 'r') as todo:
            for line in todo:
                line = line.strip()
                #Checks for the only numerical value ID
                try:
                    value = int(line) 
                except ValueError:
                    if line == 'p' or line == 'i' or line == 'c':
                        if line == 'p':
                            status.append('In-Progress')
                        elif line == 'i':
                            status.append('Incomplete')
                        elif line == 'c':
                            status.append('Complete')
                    elif len(line) < 10:
                        category.append(line)
                    elif len(line) > 10:
                        description.append(line)
                else:
                    id.append(value)
                    idCount = idCount + 1

#Complete rewrites the todo list file if called upon
#Used for commands that require the user to change existing items
def file_rewrite():
    with open(file, 'w') as todo:
        for i in id:
            if i == 1:
                todo.write(str(id[i-1]) + '\n')
            else:
                todo.write('\n' + str(id[i-1]) + '\n')
            if status[i-1] == 'In-Progress':
                todo.write('p' + '\n')
            elif status[i-1] == 'Incomplete':
                todo.write('i' + '\n')
            elif status[i-1] == 'Complete':
                todo.write('c' + '\n')
            todo.write(category[i-1] + '\n')
            todo.write(description[i-1])

#The function of the display argument
if args.display:
    for i in id:
        print(f"ID: {id[i-1]} | Category: {category[i-1]} | Status: {status[i-1]}")
        print(description[i-1])
        print("--------------------------------------------------------------------")
    print()

#The function of the add argument
if args.add:
        idCount = idCount + 1

        while True:
            newDescription = input('Description: ')
            if len(newDescription) <= 10:
                print('Must be more that 10 characters!')
                print()
            else:
                break
        
        while True:
            newCategory = input('Category: ')
            if len(newCategory) > 10:
                print('Must be less that 10 characters!')
                print()
            else:
                break
        
        while True:
            newStatus = input('Status: ')
            if newStatus.lower() == 'p' or newStatus.lower() == 'in-progress':
                newStatus = 'In-Progress'
                fileWrite = 'p'
                break
            elif newStatus.lower() == 'i' or newStatus.lower() == 'incomplete':
                newStatus = 'Incomplete'
                fileWrite = 'i'
                break
            elif newStatus.lower() == 'c' or newStatus.lower() == 'complete':
                newStatus = 'Complete'
                fileWrite = 'c'
                break
            else:
                print("Please provide proper input!")
                print("p (In-Progress)")
                print("i (Incomplete)")
                print("c (Complete)")
                print()

        #Adds to the individual list representations
        description.append(newDescription)
        category.append(newCategory)
        status.append(newStatus)
        id.append(idCount)

        #Adds to the file
        with open(file, 'a') as todo:
            if idCount == 1:
                todo.write(str(id[idCount-1]) + '\n')
            else:
                todo.write('\n' + str(id[idCount-1]) + '\n')
            todo.write(fileWrite + '\n')
            todo.write(newCategory + '\n')
            todo.write(newDescription)

#The function of the status argument
if args.status == None:
    pass
elif args.status.lower() == 'p' or args.status.lower() == 'in-progress':
    status[args.id - 1] = 'In-Progress'
    file_rewrite()
elif args.status.lower() == 'i' or args.status.lower() == 'incomplete':
    status[args.id - 1] = 'Incomplete'
    file_rewrite()
elif args.status.lower() == 'c' or args.status.lower() == 'complete':
    status[args.id - 1] = 'Complete'
    file_rewrite()
else:
    print("Please provide proper input!")
    print("p (In-Progress)")
    print("i (Incomplete)")
    print("c (Complete)")
    print()

#The status of the update argument
if args.update == 1:
    print('What would you like to change the Category to?')
    userinput = input('Category: ')
    category[args.id - 1] = userinput
    file_rewrite()
elif args.update == 2:
    print('What would you like to change the Description to?')
    userinput = input('Description: ')
    description[args.id - 1] = userinput
    file_rewrite()