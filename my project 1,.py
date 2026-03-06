age = int(input("Enter the student's age: "))

if age >= 10:
    if age <= 20:
        print("The student is allowed to enroll in the class.")
    else:
        print("The student is too old and cannot enroll.")
else:
    print("The student is too young and cannot enroll.")
