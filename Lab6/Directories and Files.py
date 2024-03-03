import os
# ex1
def list_d(path):
    directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    print("Directories:")
    for directory in directories:
        print(directory)

def list_f(path):
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    print("\nFiles:")
    for file in files:
        print(file)

def list_all(path):
    print("\nDirectories and Files:")
    for root, dirs, files in os.walk(path):
        for directory in dirs:
            print(os.path.join(root, directory))
        for file in files:
            print(os.path.join(root, file))
            
p = input("Enter the path: ")
if os.path.exists(p):
    list_d(p)
    list_f(p)
    list_all(p)
else:
    print("Invalid path.")



# ex2
def check(path):
    if not os.path.exists(path):
        print("Path does not exist")
        return

    print("Path exists")

    if os.access(path, os.R_OK):
        print("Readable")
    else:
        print("Not readable")

    if os.access(path, os.W_OK):
        print("Writable")
    else:
        print("Not writable")

    if os.access(path, os.X_OK):
        print("Executable")
    else:
        print("Not executable")

path = input("Enter the path: ")
check(path)



# ex3
def check_p(path):
    if os.path.exists(path):
        print("Path exists")
        directory_name, file_name = os.path.split(path)
        print("Directory:", directory_name)
        print("Filename:", file_name)
    else:
        print("Path does not exist")


p = input("Enter the path: ")
check_p(p)



# ex4
def count_lines(filename):
    with open(filename, 'r') as file:
        line_count = sum(1 for line in file)
    return line_count


fname = input("Enter the name of the text file: ")
try:
    lines = count_lines(fname)
    print("Number of lines:", lines)
except FileNotFoundError:
    print("File not found")




# ex5
def write(fpath, data):
    with open(fpath, 'w') as f:
        for item in data:
            f.write(str(item) + '\n')

d = input().split()
fpath = input("Enter the file path: ")
write(fpath, d)




# ex6
import string

def generate_files():
    for letter in string.ascii_uppercase:
        fname = letter + ".txt"
        open(fname, "x")

generate_files()




# ex7
def copy_file(first_file, second_file):
    with open(first_file, 'r') as source:
        with open(second_file, 'w') as destination:
            for line in source:
                destination.write(line)

f1 = input("Enter the name of the source file: ")
f2 = input("Enter the name of the destination file: ")
copy_file(f1, f2)




# ex8
def deletef(path):
    if not os.path.exists(path):
        print("File does not exist.")
        return

    if not os.access(path, os.R_OK | os.W_OK):
        print("You do not have access to delete")
        return

    try:
        os.remove(path)
        print("File deleted")
    except OSError as e:
        print(f"Error: {e}")

path = input("Enter the path of the file to delete: ")
deletef(path)
