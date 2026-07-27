"""Write a program to count the total number of vowels (a, e, i, o, u) present in a given sentence."""

def vowel_counter(msg):
	count = 0
	vowels = 'aeiou'
	for character in msg:
		if character in vowels:
			count += 1
	return count
	
msg = input('Enter your sentence: ')

print(vowel_counter(msg.lower()))
			
	
	