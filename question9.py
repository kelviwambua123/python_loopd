# 9. Check for Two Numbers That Add Up to Target Sum
def has_pair_with_sum(lst, target_sum):
    for i in range(len(lst)):  # Loop through each element in the list
        for j in range(i + 1, len(lst)):  # Loop through subsequent elements
            if lst[i] + lst[j] == target_sum:  # Check if the sum of two elements equals target_sum
                return True  # Return True if a pair is found
    return False  # Return False if no pairs add up to target_sum

# Example usage
example_list = [1, 2, 3, 9]
target_sum = 5
print("Has pair with sum:", has_pair_with_sum(example_list, target_sum))
