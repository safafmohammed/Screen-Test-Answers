a=float(input("Enter first no:"))
b=float(input("Enter second no:"))
choiceop=str(input("Enter choice(+,-,*,/):"))
op=["+","-","*","/"]
if choiceop==op[0]:
    print(a+b)
elif choiceop==op[1]:
    print(a-b)
elif choiceop==op[2]:
    print(a*b)
elif choiceop==op[3]:
    print(a/b)
