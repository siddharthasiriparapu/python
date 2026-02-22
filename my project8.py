# Simple Python program: read 3 values and print them in reverse

# Read three values from the user
a = input("Enter first value: ")
b = input("Enter second value: ")
c = input("Enter third value: ")

print("You entered:")
print("a =", a)
print("b =", b)
print("c =", c)

# Reverse the order
a, b, c = c, b, a

print("\nAfter reversing:")
print("a =", a)
print("b =", b)
print("c =", c)