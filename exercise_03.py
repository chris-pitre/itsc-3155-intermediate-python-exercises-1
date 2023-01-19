def letter_count_dict(string):
    string = string.lower()
    string = string.replace(" ", "")
    count_dict = {x: string.count(x) for x in string}
    return count_dict

user_input = input("Enter a string: ")
print(letter_count_dict(user_input))

