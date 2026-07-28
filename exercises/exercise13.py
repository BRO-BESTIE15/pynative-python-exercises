"""Iterate through a given list of numbers and print only those numbers which are divisible by 5."""

list1 = [80, 19, 54, 0, 2, 29, 64, 61, 76, 27, 61, 43, 85, 98, 65, 35, 44, 65, 83, 1]

print(list1)
print('\nNumber divisible by 5: ')
for i in list1:
	if i % 5 == 0:
		print(i)

	