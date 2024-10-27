# 1. FizzBuzz Program
def fizz_buzz():
    for i in range(1, 51):  # Loop from 1 to 50
        if i % 3 == 0 and i % 5 == 0:  # Check if divisible by both 3 and 5
            print("FizzBuzz")
        elif i % 3 == 0:  # Check if divisible by 3
            print("Fizz")
        elif i % 5 == 0:  # Check if divisible by 5
            print("Buzz")
        else:
            print(i)  # Print the number if not divisible by 3 or 5

# Run the FizzBuzz function
fizz_buzz()
