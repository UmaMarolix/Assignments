"""#recursion
def product(a,b):
   c=a*b
   while c == 10000:   
     print(c)
     print(a,b)
     break
   else: 
    print(c)
    a=a+1
    b=b+1
    product(a,b)  # calling the func recursively

a=95
b=95
product(a,b)  #calling the function for the first time


#until the value of c is equal to 10000, we need to increament the a or b

# factorial
def factorial(n=5):
  if n==0:
    return(1)
  else:
    result =1
    for i in range(1,n+1):
      result=result*i
    return(result)   

n=5
print(factorial(n))   


#rec
def recfactorial(n):
  if n==1:
     return n
  return n*recfactorial(n-1)#we r calling recursively

n=5
if n==0 or n==1:
   print("factorial of ",n,"is",1)
else:
   print("factorial of",n,"is", recfactorial(n))  

#fabonacci
n=10
a=0
b=1

for i in range(2,n+1):
   c=a+b
   print(c)
   a=b
   b=c
   print(c)
"""
#
def recfibo(n):
   if n<=1:
      return n
   else:
      return(recfibo(n-1)+recfibo(n-2))

n=int(input("enter n:\n"))
if n<=0:
   print("please enter the value")
else:
   for i in range(n):
      a=recfibo(i)
      print(a)         

