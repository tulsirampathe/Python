# factorial(5) = 5 X 4 X 3 X 2 X 1

def factorial(n):
    if(n == 1 or n == 0):
        return 1
    return n * factorial(n-1)

n = int(input("Enter a number : "))

print(f"The factorial of the number is : {factorial(n)}")