#1. variables do nt start with digits.
#2. it starts with A-Z,underscore(_),(-),a-z.
#3. variable is case sensitive.
#4. combination of digits, alphabets and underscore is allowed but we cant start variable name with starting withh digits.
#5. do not use space between variables names.

## Identifier is a name that can be used to identify pyrhon objects

#--------------------------------------------------------------------

#x=[10]
#y=[10]
#print(x is y)
#print(id(x))
#print(id(y))*/



#  is-> is used to compare address of object

#  ==-> is used to compare value of an object

#  x=10
#  print(x>>2)


#str1='python'
#print(str1.index('t',2,3))
#print(str1.index(-1))
#l1=(10,20,"aditya","ritu",30,40)
#print(l1.index(20,1,4))


# n=int(input("enter any number"))
# sum=0
# new=n

# while n>0:
#     digit=n%10
#     sum=sum+digit
#     n=n//10
# print(sum)

# if (new%sum==0):
#     print(f'{new} is a harshad number')
# else:
#     print(f'{new} is not a harshad number')
# str1=input("enter string1")
# str2=input("enter string2")
# if (sorted(str1)==sorted(str2)):
#     print("anagram")
# else:
#     print("no")    

# print("calculator program")
# a=int(input("enter first number"))
# b=int(input("enter second number"))
# c=eval(input("enter the operator symbol"))
# def add(a,b):
#     print("addition will be:",a+b)
# def subtr(a,b):
#     print("subtraction will be:",a-b)
# def multi(a,b):
#     print("multiplication will be:",a*b)
# def divid(a,b):
#     print("division will be:",a/b)
    
# if(c=="+"):
#     add(a,b)
# elif(c=="-"):
#     subtr(a,b)
# elif(c=="*"):
#     multi(a,b)
# else:
#     divid(a,b)
                 
# n=eval(input("enter any number:"))
# m=eval(input("enter any other number:"))
# temp=m
# m=n
# n=temp
# print("n:",n)
# print("m:",m)

# a=eval(input("enter first number"))
# b=eval(input("enter second number"))
# c=eval(input("enter third number"))
# if((a>b)and(a>c)):
#     print(f'{a} is largest')
# elif((b>a)and (b>c)):
#     print(f'{b} is greatest')
# elif((c>a)and(c>b)):
#     print(f'{c} is largest')
# else:
#     print("invalid data")

# n=eval(input("enter the range for natural numbers:"))
# for i in range(1,n+1):
#     print(i,end=" ")

# n=eval(input("enter number:"))
# sum=0
# while n>0:
#     digit=n%10
#     sum=sum+1
#     n=n//10
# print(sum)
        

# n=int(input("enter any number"))
# x=0
# y=1
# z=0
# while(n>=z):
#     print(z)
#     x=y
#     y=z
#     z=x+y

# n=int(input("enter the number of rows:"))
# for i in range(n):
#     for j in range(i):
#         print(" ",end=" ")
#     for j in range(n-i):
#         print("*",end=" ")
#     for j in range(n-i):
#         print("*",end=" ")
#     print() 

# def addi(x):
#     if x%2==0:
#         return x+1
#     else:
#         return x+2
#     return x+2

# l1=[1,2,3,4,5,6,7,8,9,10]
# res=map(addi,l1)
# print(list(res))

# def display(x,y,z):
#     return x+y+z

# l1=[2,4,6]
# l2=[1,2,3]
# l3=[4,5,6,7,8]

# res=map(display,l1,l2,l3)
# print(list(res))
    
def display(x,y):
    return x**y

l1=[2,4,6]
l2=[1,2,3]
res=map(display,l1,l2)
print(list(res))



