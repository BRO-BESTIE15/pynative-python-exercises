"""Iterate through the first 10 numbers (0–9). In each iteration, print the current number, the previous number, and their sum."""

previous_num=0
for num in range(10):
	print(f"Current number: {num}")
	print(f"Previous number: {previous_num}")
	print(f"There sum is {num+previous_num}")
	print('-'*20)
	previous_num = num