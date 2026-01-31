def linear_search(rno,target):
    for i in range(len(rno)):
        if rno[i]==target:
            return i
    return -1

n=int(input("enter total no of students:"))
roll=[]
for i in range(n):
    n1=int(input("enter the roll .no of student:"))
    roll.append(n1)
print(roll)
target=int(input("Enter roll no. to be searched:"))

res=linear_search(roll,target)
if res!=-1:
    print("student with roll.no is found at index:",res)
else:
    print("no student found with this roll .no")


