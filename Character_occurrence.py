string=(input("enter a word: "))
char=input("enter the character to find it's occurenc: ")
i=0
count=0
while(i<len(string)):
    if(string[i] == char):
        count = count+1
    i=i+1
print("total number of occurenc = ",count)