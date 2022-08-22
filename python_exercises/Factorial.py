def factorial(num: int):
    import math
    return math.factorial(num)


n = int(input("Enter number: "))
if n > 0:
    print("Factorial of", n, "is", factorial(n))
else:
    print("This number doesnt have a factorial")



