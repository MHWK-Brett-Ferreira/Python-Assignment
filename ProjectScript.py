import argparse
import ProjectFunctions
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--add", type=str, choices=["Yes", "No", "yes", "no"])
parser.add_argument("--list", type=str, choices=["Yes", "No", "yes", "no"])
parser.add_argument("--search", type=str, nargs='?')
# parser.add_argument("--file", type=str,)
args = parser.parse_args()

keyword = args.search

if args.add:
 ProjectFunctions.taskAdd()
if args.list:
    ProjectFunctions.taskList()
if keyword:
    ProjectFunctions.taskSearch(keyword)