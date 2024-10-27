# 5. Print Keys with Even Values in a Dictionary
def print_even_keys(d):
    for key, value in d.items():  # Loop through each key-value pair in the dictionary
        if value % 2 == 0:  # Check if the value is even
            print(key)  # Print the key if the value is even

# Example usage
sample_dict = {'a': 2, 'b': 3, 'c': 4}
print_even_keys(sample_dict)
