print("grading system")
print("enter marks for 5 subjects")
s1=int(input())
s2=int(input())
s3=int(input())
s4=int(input())
s5=int(input())

tot=s1+s2+s3+s4+s5
avg=tot/5
print("total = ",tot)

if(avg >= 91 and avg <= 100):
    print("your grade is A1")

elif(avg >= 81 and avg <= 91):
    print("your grade is A2")

elif(avg >= 71 and avg <= 81):
    print("your grade is B1")

elif(avg >= 61 and avg <= 71):
    print("your grade is B2")

elif(avg >= 51 and avg <= 61):
    print("your grade is C1")

else:
    print("your are below 50%")