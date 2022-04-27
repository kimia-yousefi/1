ntimes = int(input("How many times? "))
# first two terms
n1, n2 = 0, 1
count = 0
# check if the number of terms is valid
if ntimes <= 0:
   print("Please enter a positive integer")
elif ntimes == 1:
   print("Fibonacci sequence upto",ntimes,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < ntimes:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1