import os


folder = "sorted"
files = [file for file in os.listdir(folder) if file.endswith('.txt')]
files_data = []

for file in files:
    full_path = os.path.join(folder, file)
    with open(full_path, encoding='utf-8') as f:
        lines = f.readlines()
        files_data.append([file,len(lines),lines])

files_data_sorted = sorted(files_data, key=lambda x: x[1])

with open("result.txt", "w") as f:
    for data in files_data_sorted:
        f.write(data[0] + "\n")
        f.write(str(data[1]) + "\n")
        f.writelines(data[2])





