# 4. Reverse Each String in a List
def reverse_strings(strings):
    reversed_list = []  # Initialize an empty list to store reversed strings
    for string in strings:  # Loop through each string in the input list
        reversed_list.append(string[::-1])  # Reverse and add the string to the new list
    return reversed_list  # Return the list of reversed strings

# Example usage
strings = ["apple", "banana", "cherry"]
print("Reversed strings:", reverse_strings(strings))
