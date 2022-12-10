# script to read all .tsv (tab seperarated) files in current directory as text files
# perform some basic text processing (removing lines with :) and write the results to a new file

import os

for file in os.listdir("."):
    if file.endswith(".tsv"):

        with open(file) as f:
            lines = [line for line in f if ':' not in line]
        f.close()

        with open(file, 'w') as f:
            f.writelines(lines)
        f.close()