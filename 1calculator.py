def plus(a,b):
    return a+b

def dividtion(a,b):
    return a/b

def subtraction(a,b):
    return a-b

def multipliplication(a,b):
    return a*b



x=int(input("Enter First number: "))
y=int(input("Enter Second number: "))
operation=input("Enter operation (basic operations) " )

if operation=="+":
    print("Answer : ",plus(x,y))

elif operation=="-":
    print("Answer : ",subtraction(x,y))

elif operation=="*":
    print("Answer : ",multipliplication(x,y))

elif operation=="/":
    print("Answer : ",dividtion(x,y))

else:
    print(" you entered and Invalid Operation!")