"""Write a function to remove characters from a string starting from index 0 up to n and return a new string."""

def remove_n(word,n):
	new_word = word[n::]
	return new_word
	
print(remove_n(
str(input("Enter the word: ")).strip(),
int(input("Enter the index number: "))
))

