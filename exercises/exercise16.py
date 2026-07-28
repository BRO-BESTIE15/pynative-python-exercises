"""Write a program to check if a given number is a palindrome (reads the same forwards and backwards)."""

def palindrome_check(num):
	num = str(num)
	return num == num[::-1]
	
num = int(input("Enter a number: "))
print(palindrome_check(num))
