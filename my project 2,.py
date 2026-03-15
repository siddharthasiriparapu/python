# Program: Calculate n powers of a given number

number = int(input("Enter the base number: "))
n = int(input("How many powers do you want to calculate? "))

print(f"\nThe first {n} powers of {number} are:\n")

for i in range(1, n + 1):
    result = number ** i
    print(f"{number}^{i} = {result}")

