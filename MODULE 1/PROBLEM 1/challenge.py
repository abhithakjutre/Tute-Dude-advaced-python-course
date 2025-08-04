
'''
# convert celsius into forenheit


c = float(input("Celsius: "))
f=(c * 9/5) + 32
print("Forenheit: ",f)


# convert forenheit into celsius


f = float(input("Foreheit: "))
c= (f - 32) * 5/9
print("Celsius: ",c)


'''

# Make a Simple Interest calculator
p = int(input("Enter Principal: "))
r = int(input("Enter Rate of Interest: "))
t = int(input("Enter Time(in year): "))
si = (p*r*t)/100
print("Simple Interest is:",si)
