'''
sum(n) = 1 + 2 + 3 + 4 + 5.... + n
'''

def sum(n):
    if(n == 1):
        return 1
    return sum(n-1) + n

n = int(input("Enter a number : "))

print(f"Sum of {n} natural number : {sum(n)}")