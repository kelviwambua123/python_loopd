# 6. Largest Number in a Tuple
def largest_in_tuple(numbers):
    largest = numbers[0]  # Assume the first number is the largest
    for number in numbers:  # Loop through each number in the tuple
        if number > largest:  # Check if the current number is greater than the largest so far
            largest = number  # Update largest if current number is greater
    return largest  # Return the largest number found

# Example usage
num_tuple = (10, 20, 30, 40, 50)
print("Largest number:", largest_in_tuple(num_tuple))
