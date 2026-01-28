# Ask the user to enter a character 
char = input("Enter a character: ") 
# Check if the input is a single character 
if len(char) != 1: 
 print("Please enter only one character.") 
elif char.isalpha(): 
   print("The character is an alphabet.") 
else: 
   print("The character is is a number")