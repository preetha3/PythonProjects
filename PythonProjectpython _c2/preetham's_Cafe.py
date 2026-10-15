import sys
from datetime import datetime

menu_items =  {

    'pizza':390,
    'pasta':400,
    'burgers':129,
    'apple':210,
    'banana':190,
    'apple juice':180,
    'tea':30,
    'coffee':40,
    'milk':45,
    'boost':30,
    'bingo':35,
    'mango':40,
}
print(f"*******************************************")
print("date" , datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
print(f"*******************************************")
print("Welcome to preetham's Cafe")
print("pizza    :390\t  pasta   :400\t  burger  :129\t   apple   :210\t")
print("banana   :190\t  apple juice:180\t  tea   :30\t  coffee    :40\t")
print("milk     :45\t   boost    :30\t   bingo   :35\t  "" mango   :40\t")

Order_total = 0

item_1 = input("Please enter your order: ")

if item_1.lower() in menu_items:
    Order_total += menu_items[item_1.lower()]
    print(f"Order Total: {item_1.lower()} has been added to your order.")
else:
    print(f"Order Total: {Order_total} item is not available yet.")

another_order = input("Would you like to add another order? (Yes/No):")

if another_order == "yes" or another_order == "Yes" or another_order == "y":
    item_2 = input("Please enter your order:")
    if item_2.lower() in menu_items:
        Order_total += menu_items[item_2.lower()]
        print(f"Order Total: {Order_total} has been added to your order")
    else:
        print(f"Order Total: {Order_total} item is not available yet")
elif another_order == "no" or another_order == "No" or another_order == "n":
    print("Thank you for your order")
else:
    print("Invalid input please t")

print(f"*******************************************************")
print(f"The total amount of item to pay is {Order_total}")
print(f"*******************************************************")
print(f"Thank you for your order")