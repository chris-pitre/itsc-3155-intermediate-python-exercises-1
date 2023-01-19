# Chris Pitre
# Intermediate Python Exercises 1
# Exercise 3

def letter_count_dict(string):
    """
    Returns a dictionary counting each instance of a character
    in a string in all lowercase without spaces

    Parameter string: String for each letter to be counted
    """
    string = string.lower()
    string = string.replace(" ", "")
    count_dict = {x: string.count(x) for x in string}
    return count_dict

user_input = input("Enter a string: ")
print(letter_count_dict(user_input))

