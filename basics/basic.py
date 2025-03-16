#SLICING OF THE STRING

#str1='pythonista'
#print(str1[3:7:-1])
#print(str1[7:3:-1])
#print(str1[6:2:-1])                                                            


#str1='aditya pathak'
#print(str1.count('a'))

#l1=[10,20.5,'yogiji']
#l1.insert(0,'neeraj')
#print(l1)

#l1=[10,20,20.5,2,8,6,1]
#l1.remove(20.5)
#l1.clear()
#l2=l1.copy()
#print(l2)
#print(id(l1))
#print(id(l2))

#DICTIONARIES

#d1={"name":"aditya","age":32,"quali":"btech"}
#print(max(d1))
#print(min(d1))
#print(len(d1))
#print(type(d1))
#print(id(d1))
#print(d1.popitem())

#x=int(input("enter first no"))
#print(x)
#y=int(input("enter second number"))
#print(y)
#if(x>y):
#print("first value is greater",x)
#else:
#print(f"`{y}second value is greater"
#n=int(input("enter a number"))
#digit=0
#while(n>0):
#    digit=digit+1
#   n=n//10
#print(digit)
#print(n)


# n=int(input("enter any number"))
# x=y=n
# digit=0
# while n>0:
#     digit=digit+1
#     n=n//10
# sum=0
# while y>0:
#     last_digit=y%10
#     sum=sum+last_digit**digit
#     y=y//10
# if x==sum:
#     print(f"{x} is armstrong")
# else:
#     print(f"{x} is not armstrong")
        


# def square(n):
#     return n**2

# n=eval(input("enter any number:"))

# res=map(square,n)
# print(list(res))


# def display(x,y,z):
#     return x+y+z

# l1=[2,4,6]
# l2=[1,2,3]
# l3=[4,7,2,8,6,9]

# res=map(display,l1,l2,l3)
# print(list(res))

# def new():
#     yield "neeraj"
    
# x=new()
# #print(x.__next__())
# print(next(x))
    
    
# def even(n):
#     i=0
#     while i<=n:
#         if i%2==0:
#             yield i
#         i=i+1
        
        
# result=even(10)
# print(result.__next__())


def outer_fun(fun):
    def inner_fun(x,y,z):
        
        
    
    
    
