print("count_the_notes of diffrent denomination")
amount=int(input("please enter amount:"))
note1=amount//100
note2=(amount%100)//50
note3=((amount%100)%50)//10
print("note of 100=", note1)
print("note of 50=", note2)
print("note of 10=", note3)