"""

students average

"""

# import operator 



# s1 = input("shoamre daneshjuyi aval: ")
# a1 = input("moadele daneshjuye aval: ")

# s2 = input("shomare daneshjuyi dovom: ")
# a2 = input("moadele danesjuye dovom: ")

# s3 = input("shomare daneshjuyi sevom: ")
# a3 = input("moadele danesjuye sevom: ")

# s4 = input("shomare daneshjuyi chaharom: ")
# a4 = input("moadele danesjuye chaharom: ")

# a = {s1:a1, s2:a2, s3:a3, s4:a4}

# print(max(a.iteritems(),key=operator.itemgetter(1))[0])






# a=[]

# n=int(input("Enter number of students:"))

# for i in range(1,n+1):
#     b=int(input("Enter average:"))
#     a.append(b)

# a.sort()

# if a[n-2] > 20:
#     print("moadel nemitavanad az 20 bala tar bashad!")
# else:
#     print("Second largest average is:",a[n-2])



num = input("enter how many students: ")
students=[]
averages=[]


for i in num:
    name = input("enter name of student " + i+" :")
    students.append(name)
    average = int(input("enteraverage of student " + i+" :"))
    averages.append(average)
for i in num:
    print("students[i]",':',"averages[i]")


