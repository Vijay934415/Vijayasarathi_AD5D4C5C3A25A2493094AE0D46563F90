# 1.1 Implement a recursive funtion to calculate the factorial of a given number.




def fact(n):
  if n==0 or n==1:
   return 1
  else:
   return n*fact(n-1)
number=2
res=fact(number)
print("The Factorial of {} is {}".format (number,res))