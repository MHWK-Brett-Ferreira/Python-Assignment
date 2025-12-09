import time

def taskAdd():
    try:
        with open("tasks.txt", "r") as f:
            f.read()
    except FileNotFoundError:
        print("Your task file could not be found.")
        return
    except UnicodeDecodeError:
        print("Your file or parts of your file have been corrupted.")
        return
    entry = ""
    while entry == "":
        entry = input("Enter your task or project to add to file: ")
        if entry == "":
            print("You cannot add a blank entry")
            continue
        else:
            duedate = ""
            while duedate == "":
                duedate = input("Enter your task or project's due date (Ex. 2025-12-08): ")
                if duedate == "":
                    print("You cannot add a blank due date")
                continue
            else:
                with open("tasks.txt", "a") as f:
                    print("")
                    print("Your entry was successfully added!")
                    f.write(f"{entry} | Due Date: {duedate} | Entry Added: {time.strftime('%c')}\n")
def taskList():
    try:
        with open("tasks.txt", "r") as f:
            print("")
            print("Here is a list of your tasks")
            print("----------------------------")
            print("")
            print(f.read())
            print("")
            print("End of task list")
            print("----------------------------")
            print("")
    except FileNotFoundError:
        print("Your task file could not be found.")
        return
    except UnicodeDecodeError:
        print("Your file or parts of your file have been corrupted.")
        return
def taskSearch(keyword):
    try:
        with open("tasks.txt", "r") as f:
            storefile = f.readlines()
    except FileNotFoundError:
        print("Your task file could not be found.")
        return
    except UnicodeDecodeError:
        print("Your file or parts of your file have been corrupted.")
        return
    print("Searching for Keyword....")
    print("")
    found = 0
    for lines in storefile:
        findword = lines.find(keyword)
        if findword != -1:
            found = 1
            print(lines)
    if found == 1:
        print("")
        print("Your keyword was found!")
    else:
        print("Sorry, no keyword found")