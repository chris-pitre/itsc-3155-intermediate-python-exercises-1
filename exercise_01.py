# Chris Pitre
# Intermediate Python Exercises 1
# Exercise 1

def get_unique_list(data_list):
    """
    Returns a list of unique items from the list given.

    Parameter data_list: list to be used
    """
    data_list = set(data_list)
    data_list = list(data_list)
    return data_list

my_list = [1, 2, 3, 2, 1, 4]
unique_list = get_unique_list(my_list)
print(unique_list)