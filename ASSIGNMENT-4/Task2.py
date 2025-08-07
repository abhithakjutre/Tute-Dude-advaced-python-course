txt1 = input("Enter text to write the file: ")
path = "output.txt"
with open(path,"w") as file:
    output = file.write(txt1)
    print(f"Data Successfully written to {path}.")

text2 = input("Enter additional text to append: ")
with open(path,"a") as file:
    output2 = file.write(f"\n{text2}")
    print(f"Data Successfully appended.")

print(f"Final content of {path}: ")
with open(path, "r") as file:
    content = file.read()
    print(content)