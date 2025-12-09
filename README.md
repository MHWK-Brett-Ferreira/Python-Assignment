# Python-Assignment
Project Overview
This project is a cli interface program that adds tasks to a specified .txt file. It takes arguments to let you:
- Add tasks to your file
- List the tasks currently in your file
- Search the file for keywords

Installing
This program requires Python version 3+, it must be installed for you to run this program. You also need to download the ProjectScript.py, ProjectFunctions.py and tasks.txt file. Make sure they are all within the same folder.

Files 
ProjectScript.py 
The main script. Handles command line arguments and calls the functions in 

ProjectFunctions.py
Contains the functions:
**taskAdd()** – Add a new task or project to the tasks.txt file, 
**taskList()** – Display all tasks in the tasks.txt file, 
**taskSearch(keyword)** – Search tasks by a keyword in the tasks.txt file

tasks.txt
Text file used to store tasks. Each line represents one task entry.

How to run

1. Place all files in a folder
2. Enter into your folder where the files are stored in the CMD prompt, or open them in your favourite IDE (Pycharm for example)
3. Run **python ProjectScript.py [argument]** with your selected arguments
   
Arguments

**--add**
Adds your entry to the tasks.txt file with a local timestamp. Must be run with either of these options Yes or yes. You will be prompted to add your entry and due date
Ex.
python ProjectScript.py --add Yes


**--list**
Lists your entries from the tasks.txt file. Must be run with either of these options Yes or yes.
Ex.
python ProjectScript.py --list Yes

**--search**
Searches your entries from the tasks.txt file for a keyword or number. When running numbers they must be entered in quotes (Ex. "9"). Word strings do not need quotes. Only accepts one letter or word.
Ex. Command
python ProjectScript.py --Search Hello

Configurations
You can add extra arguments if you like. The argparse module is already pre-installed. Follow the same format as the ProjectScript or read the Python documentation on the argparse module.

Python Assignment
