a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print("Sum of the two numbers: ",a+b)
print("Difference between two numbers is: ",a-b)
print("Multiplication of the two numbers: ",a*b)
print("Division of two numbers is: ",a/b)

print("A simple interest calculation.")
print("*******************************")
#this a simple interest calculater
p = float(input("Enter the principal amount: "))
r = int(input("Enter the rate of interest: "))
t = float(input("Enter the time period in months: "))
interest = (p*r*t)/100
print("The interest is: ",interest)
print("*******************************")
print("Generating multiplication table.")
a = int(input("Enter a number to generate a multiplication table: "))
for i in range(1,11):
    print(a,"x",i,"=",a*i)