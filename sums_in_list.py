# 3. Sum of Numbers in a List
def sum_of_list(nums):
    total = 0  # Initialize total to 0
    for num in nums:  # Loop through each number in the list
        total += num  # Add the number to total
    return total  # Return the total sum

# Example usage
nums = [1, 2, 3, 4, 5]
print("Sum:", sum_of_list(nums))
