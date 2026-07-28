"""Create a new list from two given lists such that the new list contains odd numbers from the first list and even numbers from the second list."""

def list_merger(list1, list2):
	result_list = []

	for i in list1:
		if (i%2) != 0:
			result_list.append(i)
		
	for x in list1:
		if x%2 == 0:
			result_list.append(x)
			
	return result_list
			
			
list1 =  [80, 72, 66, 65, 17, 89, 86, 71, 36, 3, 15, 48, 22, 59, 71, 9, 40, 48, 90, 63, 17, 22, 18, 20, 19, 52, 12, 32, 13, 13, 19]

list2 = [64, 18, 51, 2, 78, 68, 66, 73, 71, 28, 56, 14, 22, 63, 91, 86, 79, 15, 93, 16, 86, 14, 63, 84, 25, 7, 46, 77, 83, 31, 88]

print(list_merger(list1, list2))

