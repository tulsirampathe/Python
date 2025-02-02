a = int(input("Enter you age: "))

# If elif else ladder

if( a >= 18):
    print("Yor are above the age of consent")
    print("Good for you")
    
elif( a < 0):
    print("Yor are entering an invalid negative age")

elif( a == 0):
    print("Yor are entering 0 which in a not valid  age")

else:
    print("Your are below the age of consent")
    
    
print("End of program")