# ####
# Lists are used to store lists of related information
# The list can contain data variables of different types
# ####

friends = ["Kevin", "Martin", "Karen", "George", "Steve", "Elvis"]
print("Print out array:", friends)
# Access the list elements using their indices e.g Martin(index 1)
print("Data element at index 1:", friends[1])
# Use negative indices. They start from the right side
print("Using negative indices:", friends[-1], friends[-2])
# Select items from one index and the subsequent items from that index
print("Range from index 1:", friends[1:])
# Access elements within a range
print("Range from index 1-4:", friends[1:4])
# Modify a value
print("Before modification:", friends[4])
friends[4] = "Mike"
print("After modification:", friends[4])

luckyNo = [4, 5, 7, 3, 6, 5]
# Add an element to the list
friends.append("Creed")
print("Appended list:", friends)
# Add element at a specific index
friends.insert(2, "John")
print("Inserted list:", friends)
# Remove an element
friends.remove("George")
print("Removed \"George\" from list:", friends)
# Pop out the last element of the list
friends.pop()
print("Pops out last element of list:", friends)
# Find index of list element
print("Index of Mike is:", friends.index("Mike"))
# Count the number of times an element is defined in a list
print("\"Elvis\" is defined ", friends.count("Elvis"), "times.")
# Sort list alphabetically or numerically
friends.sort()
luckyNo.sort()
print("Sorted list:", friends)
print("Sorted number list:", luckyNo)
# Reverse the order of the list
luckyNo.reverse()
print("Reversed list order:", luckyNo)
# Copy a list to another list
friendsList = friends.copy()
print("Copied list:", friendsList)
# Append one list to another
friends.extend(luckyNo)
print("Extended list:", friends)
# Clear list
friends.clear()
print("Cleared list:", friends)
