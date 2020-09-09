a=int(input("Enter integer:"))
if(a%2==0):
    print(list(range(1,(2*a-2),2)))
else:
    print(list(range(1,2*a,2)))