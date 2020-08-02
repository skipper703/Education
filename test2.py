import os, os.path
w = open("answer.txt", "w")
print(os.getcwd())
os.chdir("test")
lst = []
for current_dir, dirs, files in os.walk("."):
    for file_name in files:
        if file_name.endswith(".py"):
            if current_dir not in lst:
                lst.append(current_dir)
for i in range(len(lst)):
    w.write(lst[i])
    w.write('\n')
