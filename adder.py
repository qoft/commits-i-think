# Created by RickyBGamez (https://github.com/RickyBGamez/)
# This script is licensed under the GNU General Public License v3.0.
# Check the GitHub repository for more information. (https://github.com/RickyBGamez/Commit-Bot)

### Configuration
# Logging Options
LOG = True
LOG_FILE = "commit_bot.log"

# Commit Options
NO_COMMIT_CHANCE = 0.1 # 10% chance of NOT committing to GitHub.
MAX_COMMITS = 500 # Maximum number of commits that can be made.

# Cron job.
CRON_JOB_TIME = "0 12 * * *" # Every day at 12:00 pm.

# Output File
OUTPUT_FILE = "commit_bot.txt"

from os import system # Executing the Git commands.
from datetime import datetime # Date and time for our file.


i = 0
def create_commit():
    global i
    while True:
        system("git pull -X theirs")
        for i in range(random.randint(1, MAX_COMMITS)):
            with open(OUTPUT_FILE, "w") as f:
                f.write(str(datetime.now()))
            system(f"git add {OUTPUT_FILE}")
            system(f"git commit -m \"Update {OUTPUT_FILE}\"")
        system("git pull -X theirs")
        system("git push")

create_commit()