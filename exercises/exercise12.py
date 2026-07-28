"""Write a function to return True if the first and last number of a given list is the same. If the numbers are different, return False."""
def list_check(data):
	return data[0] == data[-1]
list1 = [10, 12, 85, 69, 10]
list2 = ['HI' , 48, 94, 79.8]
check1 = list_check(list1)
check2 = list_check(list2)
print(f'List: \n{list1} \nResult: \n{check1}')	
print(f'List: \n{list2} \nResult: \n{check2}')