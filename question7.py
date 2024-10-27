# 7. Remove Duplicates from a List
def remove_duplicates(lst):
    unique_list = []  # Initialize an empty list to store unique elements
    for item in lst:  # Loop through each item in the input list
        if item not in unique_list:  # Check if the item is already in unique_list
            unique_list.append(item)  # Add item if it's not a duplicate
    return unique_list  # Return the list of unique items

# Example usage
example_list = [1, 2, 2, 3, 4, 4, 5]
print("Without duplicates:", remove_duplicates(example_list))
