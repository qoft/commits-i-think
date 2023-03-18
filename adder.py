import random, multiprocessing, os
OUTPUT_FILE = f"data/output_{random.randint(0, 100)}.txt"
if not os.path.exists("data"):
    os.makedirs("data")
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

if __name__ == "__main__":
    for i in range(5):
        multiprocessing.Process(target=create_commit).start()
        