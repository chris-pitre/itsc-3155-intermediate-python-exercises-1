# Chris Pitre
# Intermediate Python Exercises 1
# Exercise 4

user_input = []

for i in range(5):
    break_case = True
    """
    Input validation
    The terminal asks the user for an input, and if the input
    is not an integer, it throws a ValueError exception and prompts
    the user to try again. When an integer is successfully entered,
    break_case is set to false and the while loop is broken
    """
    while break_case:
        try:
            user_input.append(int(input(f"Enter int #{i+1}: ")))
            break_case = False
        except ValueError:
            print("Invalid input. Please enter an int.")

user_sum = sum(user_input)
print(f"Your sum is {user_sum}")