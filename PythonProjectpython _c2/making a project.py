num = int(input("enter a number: "))
for i in range(1,num+1):
    for j in range(1,i+1):
        print(j,end=" ")

print()

#to find positive or negative number
num = float(input("Enter a number: "))

if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")

n = int(input("Enter a number: "))
sum = 0
for i in range(1, n + 1):
    sum += i
print("Sum of natural numbers:", sum)

string = input("Enter a string: ")
word_count = len(string.split())
print("Number of words:", word_count)

import math

def is_perfect_square(n):
    root = math.isqrt(n)
    return root*root == n

number = int(input("Enter the number: "))
if is_perfect_square(number):
    print("The number is perfect square")
else:
    print("The number is not perfect square")

def is_perfect_cube(n):
    root = round (n**(1/3))
    return root ** 3 == n
n = int(input("Enter a number: "))
if is_perfect_cube(n):
    print("The number is Perfect cube")
else:
    print("The number is Not a perfect cube")
