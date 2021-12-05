# Lists:
# lists can be written several ways:
# First, you can have items in the list of all the same type:
["Squirrel", "Rabbit", "Mouse"]
# You can also have multiple types of items in a list:
[7, "forest", 3.43]
# Believe it or not you can even have a list inside another list
# this is calles a nested list:
[1, 2, 3, [4, 5]]
# you can assign a list to a variable:
shoe_brands = ["Nike", "Adidas", "Puma", "Vans"]
print(shoe_brands)
# Lists use 'in' and 'not in' operators:
print("Nike" in shoe_brands)
print("New Balance" in shoe_brands)
print("New Balance" not in shoe_brands)
# lists can be manipulated using operations used in mathematics:
list_one = ["A", "B", "C"]
list_two = ["D", "E", "F"]
# addition: adds the lists together into one list
list_three = list_one + list_two
print(list_three)
# lists can use multiplication too:
print(list_one * 4)
# you can also type out a list and multiply:
print([4, 5] * 2)
# the ':' operator is used for slicing lists:
# I should preface this by saying:
# when a computer reads the number of the place in line in the list,
# it starts from 0 and counts up:
num_list = [ ]