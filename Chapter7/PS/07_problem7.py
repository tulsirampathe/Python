n = int(input("Enter the number: "))

'''
k = 1
for i in range(1, n+1):
    
    s = ""
    for j in range(n-i):
        s += " "

    for j in range(k):
        s += "*"
        
    k += 2
    print(s)
    
    '''
    
# Simple way to do this:

for i in range(1, n+1):
    print(" " * (n-i), end="")
    print("*" * (2 * i - 1), end="")
    print("")