# 10. Convert List of Tuples to Dictionary
def tuples_to_dict(tuples):
    result_dict = {}  # Initialize an empty dictionary
    for key, value in tuples:  # Loop through each tuple
        result_dict[key] = value  # Assign the tuple's first element as key, second as value
    return result_dict  # Return the constructed dictionary

# Example usage
example_tuples = [("apple", 5), ("banana", 7), ("cherry", 3)]
print("Dictionary:", tuples_to_dict(example_tuples))
