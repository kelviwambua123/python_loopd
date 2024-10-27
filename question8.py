# 8. Get Keys with Values Greater Than n
def keys_greater_than(d, n):
    result_keys = []  # Initialize an empty list to store matching keys
    for key, value in d.items():  # Loop through each key-value pair in the dictionary
        if value > n:  # Check if the value is greater than n
            result_keys.append(key)  # Add the key to result_keys if condition is met
    return result_keys  # Return the list of keys with values greater than n

# Example usage
sample_dict = {'a': 5, 'b': 12, 'c': 3}
n = 4
print("Keys with values greater than", n, ":", keys_greater_than(sample_dict, n))
