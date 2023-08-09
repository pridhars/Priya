#while loop
i=1
while i<=10:
    print(i)
    i=i+1
i=1
n=15
while i<=10:
     print(n,"*",i,"=",n*i)
     i=i+1
#list
l1=[1,2,3,4,5]
i=4
while i<len(l1):
    l1[0]=l1[0]+100
    l1[1]=l1[1]+100
    l1[2]=l1[2]+100
    l1[3]=l1[3]+100
    l1[4]=l1[4]+100
    i=i+1
    print(l1)
#for loop
l1=['orange','green','red']
l2=['book','chair','phone']
for i in l1:
    for j in l2:
        print(i,j)
#even or odd
num=int(input("enter the number:"))
if (num%2)==0:
    print(num,"is even")
else:
    print(num,"is odd")
#check positive (or) nrgative
num=int(input("enter the number"))
if num>0:
    print("positive num")
elif num==0:
    print("zero")
else:
    print("negative num")
#factorial
fact=1
if num<0:
    print(" the factorial does not eexists in negtive")
elif num==0:
    print("the factorial of 0 is 1")
else:
    print("the factorial of",num,"is",fact)
#reversing a number
n=int(input("enter the number"))
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
print("reverse of no is",rev)
#palindrome numbers
n=int(input("enter the number"))
temp=n
rev=0
while temp!=0:
    rev=(rev*10)+(temp%10)
    temp=temp//10
if(n==rev):
    print("the no is palindrome")
else:
    print("the no is not a palindrome")
#palindrome string
n=str(input("enter the string"))
if(n==n[::-1]):
      print("The string is a palindrome")
else:
      print("The string isn't a palindrome")
#fibonacci
n = int(input("enter the number"))
num1 = 0
num2 = 1
next_number = num2
count = 1
while count<=n:
	print(next_number, end=" ")
	count += 1
	num1, num2 = num2, next_number
	next_number = num1 + num2
print()
