import os
import shutil

base_pass = ""
grouped_file = {}
i = 0

for paths, dirs, files in os.walk(base_pass):
    for file in files:
        prefix = file.rpartition(".")[2]
        if prefix not in grouped_file:
            grouped_file[prefix] = []
        full_file_path = os.path.join(paths, file)
        grouped_file[prefix].append(full_file_path)


for ext, file_list in grouped_file.items():
    print(f"{ext}: {file_list}")
    folder_path = os.path.join(base_pass, ext)
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
    for file in file_list:
        old_path = os.path.basename(file)
        new_path = os.path.join(folder_path, old_path)

        shutil.move(file, new_path)
        
