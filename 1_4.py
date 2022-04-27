"""
finding perfect number
"""

number = int(input("please enter number: "))

sum = 0

for i in range (1,number):
    if(number % i == 0):
        sum = sum + i

if number == sum:
    print("this is perfect number")

else:
    print("this isn't perfect number")
