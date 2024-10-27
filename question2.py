# 2. Continuously Ask for Input Until "exit" is Entered
def get_input():
    while True:  # Start an infinite loop
        user_input = input("Enter a word (or type 'exit' to stop): ")
        if user_input.lower() == "exit":  # Check if input is "exit"
            break  # Exit the loop if "exit" is entered
        print(user_input)  # Print the user's input

# Uncomment the line below to run this function interactively
# get_input()
