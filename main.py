# Exercise 3
from pathlib import Path

# import functions from utils here
from utils import count, writefile

# 1. Contstruct the path to the text file in the data directory using the `pathlib` module [2P]
d = Path('/home/mklee/git/exercise-3-Kleebaue')
data_dir = d / 'data'
output_dir = d / "solution"

# 2. Read the text file [2P]
# splitlines removes /n 
with open(data_dir / 'cars.txt', "r") as fd:
    car = fd.read().splitlines()

print(car)

# 3. Count the occurences of each item in the text file [2P]
# using counter from utils to solve task
countcars = count(car)

# 4. Using `pathlib` check if a directory with name `solution` exists and if not create it [2P]
output_dir.mkdir(parents=True, exist_ok=True) 

# 5. Write the counts to the file `counts.csv` in the `solution` directory in the format (first line is the header): [2P]
#    item, count
#    item_name_1, item_count_1
#    item_name_2, item_count_2
#    ...
# using writefile function from utils to write file 

writefile(countcars,output_dir,'Count_unique_cars.csv',"item","count")
