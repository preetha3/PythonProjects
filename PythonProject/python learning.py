letter = '''Dear <|NAME|>,
         you are selected
         <|DATE|>'''

letter = letter.replace("<|NAME|>", "Preetham")
letter = letter.replace("<|DATE|>", "24 December 1100")
print(letter)


name = "Harry is a good  boy"
print(name.find("Harry"))
print(name.find(" "))

#lists
friends = ["apple", "mango", "orange", "234", "3825", "pritham", "maaz"]
print(friends[0])

friends.append("harry")
print(friends)

li = [1, 2, 2, 3, 3, 3, 4, 4, 4, 45, 5, 5, 56, 7]
li.sort()
print(li)
li.sort(reverse=True)
li.insert(3, 333333)
print(li)

