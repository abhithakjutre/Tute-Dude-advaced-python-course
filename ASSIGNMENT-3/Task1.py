
def factorial(n):
    if n<2:
        return 1
    else:
        return n * factorial(n-1)

num = int(input("Enter a number: "))
result = factorial(num)
print(f"Factorial of {num} is: ",result)