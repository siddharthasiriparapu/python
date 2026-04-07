n = int(input("Enter the height of the triangle: "))

print("Right-angled triangle:")
for i in range(1, n + 1):
    # i stars, left aligned
    print("*" * i)

print("Mirrored right-angled triangle:")
for i in range(1, n + 1):
    spaces = n - i
    stars = i
    print(" " * spaces + "*" * stars)
