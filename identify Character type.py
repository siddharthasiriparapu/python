# Identify character type using ASCII ranges
ascii_val=(input("enter a Character:" ))
if ascii_val >= 65 and ascii_val <= 90:

    print("Type: Uppercase Letter")

elif ascii_val >= 97 and ascii_val <= 122:

    print("Type: Lowercase Letter")

elif ascii_val >= 48 and ascii_val <= 57:

    print("Type: Digit")

elif ascii_val == 32:

    print("Type: Space")

else:

    print("Type: Special Character")
