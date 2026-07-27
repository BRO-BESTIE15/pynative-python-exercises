"""Write a script that takes a list containing duplicate items and returns a new list with only unique elements."""

duplicate_data = [1, 1, 283, 287, 'hi', 'hello', 1,1, 283, 287, 'hi', 'hello', 1, 1, 283, 287, 'hi', 'hello', 1,1, 283, 287, 'hi', 'hello' ]

unique_set = set(duplicate_data)
unique_list = list(unique_set)

print(unique_list)