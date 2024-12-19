#Q3) Function to find the last position of a given substring
def find_last_position(string, substring):
    position = string.rfind(substring)  # Using rfind() to find the last occurrence
    return position

# Input
string = input("Enter the main string: ")
substring = input("Enter the substring to find: ")

# Finding the last position
last_position = find_last_position(string, substring)


if last_position != -1:
    print(f"The last position of the substring '{substring}' is: {last_position}")
else:
    print(f"The substring '{substring}' is not found in the given string.")
