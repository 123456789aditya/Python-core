# print("printing star pattern")
# n=5
# i=1
# while i<=5:
#     print("*"*i)
#     i=i+1

# n=int(input("how many rows required"))
# i=1
# while i<=n:
#      print(" "*(n-i)+"*"*i)
#      i=i+1

# n=int(input("enter no of rows:"))
# while n>=1:
#     print("*"*n)
#     n=n-1

# n=int(input("enter the number of rows"))
# i=0
# while i<n:
#     print(" "*i+"*"*(n-i))
#     i=i+1

# 

# def add(*n):
#     print(n)
#     sum=0
#     for i in n:
#         sum=sum+i
#     return sum

# x=add(2,3,4,4,6,6,5,8,2,7)
# print(x)
    

# def add(*n):
#     return n
    
# x=eval(input("enter any type"))
# result=add(*x)
# print(result)
    
# def add(*n):
#     sum=0
#     for i in n:
#         sum=sum+i
#     return sum
    
# x=eval(input("enter any type"))
# y=add(*x)
# print(y)    
    
# def details(**n):
#     for k,v in n.items():
#         print(f'my {k} is {v}')
 
        
# details(name="neeraj",age=91,quali="b-tech")

            
#-----------------------------


# x=10
# def add():
#     global y
#     y=20
#     print(x)
#     print(y)
    
# add()
# print(x)
# print(f'global variable{y}')

#----------------------

# #-----------------

#we can access the outer function value in a function by using globals keyword
def add(*n):
    sum=0
    for i in n:
        sum=sum+i
add(1,2,3,4,5,6,7,8)
        

