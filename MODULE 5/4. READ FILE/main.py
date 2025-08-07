# 1. Method
'''
file = open("read_file.txt","r")
result = file.read()
print(result)
file.close()

'''

# 2. Method
with open("read_file.txt","r") as file:
    result = file.read()
    print(result)


