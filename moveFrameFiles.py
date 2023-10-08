import os
import shutil

target = 'movie1K.keyframes.240p.v1/240p'
dest = 'dataset/framescene'

# Ensure destination directory exists
os.makedirs(dest, exist_ok=True)

# Read film names from the text file
with open('film_list.txt', 'r') as f:
    film_names = [line.strip() for line in f]

# Iterate over the film names and move matching tar files
count_moved = 0
for film_name in film_names:
    tar_file_path = os.path.join(target, film_name + '.tar')
    if os.path.exists(tar_file_path):
        shutil.move(tar_file_path, os.path.join(dest, film_name + '.tar'))
        count_moved += 1

print(f'Moved {count_moved} matching tar files to {dest}.')