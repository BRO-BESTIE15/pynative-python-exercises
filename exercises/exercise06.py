"""Write a program that calculates the factorial of a given number (e.g., 5!) using a for loop."""
def calculate_factorial(num):
	factorial = 1
	for n in range(1, num+1):
		factorial=factorial*n
	return factorial 
		

num = int(input("Enter a number to calculate factorial: "))

factorial = calculate_factorial(num)

print(f'You input: {num}, \nFactorial: {factorial}')
