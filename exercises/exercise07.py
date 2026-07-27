'''Create a list of 5 fruits. Add a new fruit to the end of the list, then remove the second fruit (at index 1).'''

fruits = ['apple', 'mango', 'kiwi', 'grapes', 'cherry']

fruits.append("watermelon")

print(f'List after adding a new fruit: \n{fruits}\n')

fruits.pop(1)

print(f'List after removing fruit at index 1: \n{fruits}')
