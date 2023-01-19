user_input = []

for i in range(5):
    break_case = True
    while break_case:
        try:
            user_input.append(int(input(f"Enter int #{i+1}: ")))
            break_case = False
        except ValueError:
            print("Invalid input. Please enter an int.")

user_sum = sum(user_input)
print(f"Your sum is {user_sum}")