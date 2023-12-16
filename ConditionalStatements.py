#Conditional Statements
#Find the Largest No b/w two numbers
'''
x = int(input("Enter No1:"))
y = int(input("Enter No2:"))

if x>y:
    print(f"{x} is largest")
elif x==y:
    print("Both Values are Same")
else:
    print(f"{y} is largest")
'''
x = int(input("Enter No1:"))
y = int(input("Enter No2:"))
z = int(input("Enter No3:"))

if x>y and x>z:
    print(f"{x} is largest")
elif y>z:
    print(f"{y} is largest")
else:
    print(f"{z} is largest")
'''
#Take a number as input and check whether the no is even or odd
x = int(input("Enter No :"))
if x%2==0:
    print("Even")
else:
    print("Odd")
'''
