import random, threading

MAX_COMMITS = 500 

OUTPUT_FILE = "commit_bot.txt"

from os import system
from datetime import datetime 
system("git pull -X theirs")
system("git clone https://github.com/qoft/commits-i-think.git")
system("adder.py")