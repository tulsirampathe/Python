n = int(input("Enter the number: "))

for i in range(2, n):
    if(n % i) == 0:
        print("Number is not Prime")
        break
else:
    print("Number is Prime")