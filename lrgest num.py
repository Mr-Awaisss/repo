n=int(input("Enter the number"))
a=0
for i in range(1,n+1):
    if (n%i==0):
        a=a+1
if (a==2):
    print("The {n} is prime")
else:
    print(f"The {n} is not prime")
        
