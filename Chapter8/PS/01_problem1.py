a = 1
b = 22
c = 3

def greatest(a, b, c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c
    
print(greatest(a, b, c))