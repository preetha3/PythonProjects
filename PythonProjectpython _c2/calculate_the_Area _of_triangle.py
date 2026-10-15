import numbers

#To find area of triangle
base = float(input("Enter the base of triangle: "))
height = float(input("Enter the height of triangle: "))
area = 0.5*base*height
print("The area of  triangle  ",area)
print("*******************************")
#To find area of rectangle
length = float(input("Enter the length of rectangle: "))
width = float(input("Enter the width of rectangle: "))
area = length*width
print("The area of rectangle:",area)
print("*******************************")
#To find area of square
length = float(input("Enter the length of square:"))
length1 = float(input("Enter the length of square:"))
print("The area of square:",length*length1)
print("*******************************")
#To find even number or odd number
num = int(input("Enter a number: "))
if num %2 == 0:
    print("Entered number is Even.")
else:
    print("Entered number is Odd.")
print("*******************************")
#To find radius of circle
import math
radius = float(input("Enter a radius: "))
area = math.pi * radius * radius
print("The Area of circle is: ", area)
print("*******************************")
#calculate the power of number
base = int(input("Enter a base: "))
exponent = int(input("Enter a exponent: "))
result = base**exponent
print("The power of ",  base ,"is ", result)
