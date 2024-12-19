#Q.2)WAP Reverse a given string

def reverse_string(input_string):


# Using slicing to reverse the string 
    return input_string[::-1]


# Input from the user
string = input("Enter a string to reverse: ")

# Display the reversed string
reversed_string = reverse_string(string)
print("Reversed String:", reversed_string)

