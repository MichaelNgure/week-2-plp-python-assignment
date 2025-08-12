# Create an empty list
my_list = []

# Append 10, 20, 30, 40 to the empty list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)

# Insert 15 at the 2nd position
my_list.insert(2, 15)
print(my_list)

# Extend the list with [50, 60, 70]
my_list.extend([50, 60, 70])
print(my_list)

# Remove last item in the list
my_list.pop()
print(my_list)

# Sort list in ascending order
my_list.sort()
print(my_list)

# Find inex of 30
index_of_30 = my_list.index(30)
print(index_of_30)
