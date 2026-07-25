"""Write a program to swap the values of two variables, a and b, without using a third temporary variable."""

a = int(input("Enter value for a : "))
b = int(input("Enter value for b: "))

print(f"a = {a} \nb = {b}")
print('-'*20)

a, b = b, a

print(f"a = {a} \nb = {b}")