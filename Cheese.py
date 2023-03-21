#adding to list
cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
cheese += 'Oke'
print(cheese)
print("This has added each character as a list item, square brackets[] are required" )
print()
cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
cheese += ['Oke']
print(cheese)
print()

#adding two more items to the list
cheese +=['Brie', 'Gouda']
print("Here's 2 more added to the list", cheese)
print()

#strings and tuple differences
print("String and Tuple Differences")
tup = 'Hello'
print(len(tup))
print("As hello is defined as a string, it prints the length of Hello = 5 characters")
tup = 'Hello',
print(len(tup))
print("Due to the comma after 'Hello' this makes the data a tuple")
print("The length of this is not characters but a data item = 1")