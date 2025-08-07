
try:
    path = "sample.txtr"
    with open(path, "r") as file:
        first_line = file.readline()
        second_line = file.readline()
        print("Reading file content: ")
        print("Line 1: ",first_line)
        print("Line 2: ",second_line)
except FileNotFoundError:
    print(f"Error: The file '{path}' was not found")

