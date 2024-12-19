#Q4)Write a Python program to create a tuple with different data types

# Create a tuple with different data types
my_tuple = ( 123, 45.67,"Hello", True, [1, 2, 3])

# Print the tuple
print("Tuple:", my_tuple)

# Print the type of each element in the tuple
print("\nTypes of elements in the tuple:\n")
for i, element in enumerate(my_tuple):
    print(f"Element {i+1}: {element} - Type: {type(element)}")

