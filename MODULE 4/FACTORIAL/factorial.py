

def factorial(n):
    if n<2:
        return 1
    else:
        return  n * factorial((n-1))

result = factorial(4)
print(result)