import random
OUTPUT_FILE = "commit_bot.txt"

from os import system
from datetime import datetime 


i = 0
def create_commit():
    global i
    while True:
        system("git pull -X theirs")
        for i in range(100):
            with open(OUTPUT_FILE, "w") as f:
                f.write(str(datetime.now()))
            system(f"git add {OUTPUT_FILE}")
            system(f"git commit -m \"Update {OUTPUT_FILE}\"")
        system("git pull -X theirs")
        system("git push")

create_commit()
