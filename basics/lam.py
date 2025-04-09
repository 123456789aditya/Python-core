# a=lambda x,y : (x+y)
# p=10
# q=20
# print(a(p,q))

#if-else condition

# n=int(input("enter any num"))
# check_num =lambda x:  'even no' if x%2==0  else 'odd'
# print(check_num(n))

# l1=[1,2,3,4,5,6]
# num=list(map(lambda x: x**2,l1))

# print(num)

# l1=[1,2,3,4,5,6]
# res=list(map(lambda x: 'even' if x%2==0 else 'odd',l1))
# print(res)

#Addition of two numbers
# l1=[1,2,3,4,5]
# l2=[4,3,2,1,3]
# res=list(map(lambda x,y: x+y,l1,l2))
# print(res)

# l1=['neeraj','raj','jai']
# res=map(lambda x: x.upper(),l1)
# print(res)

# from functools import reduce

# l1=[1,2,3,4,5,6,7,8]
# res=reduce(lambda x,y: x*y,l1)
# print(res)

# [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
# l1=[1,2,3,4]
# res=list(map(lambda x: x,l1))
# l2=[]
# l2.append(res)
# print(l2)

# i=[1,2,3,4]
# res= [i for j in range(1,5)]
# print(list(res))

# def even(n):
#     i=0
#     while i<=n:
#         if i%2==0:
#             print(i)
#         i=i+1
# x=even(10)
# print(x)    
# print(type(x))



# def new():
#     yield 10
    
# x=new()
# print(x.__next__())
# print(next(x))
        
# def even(n):
#     i=0
#     while i<=n:
#         if i%2==0:
#             yield i
#         i=i+1
        
# res=even(10)
# print(res)
# #print(list(res))
# print(next(res))
# print(next(res))

# def outer_fun(fun1):
#     def inner_fun():
#         print("Before Modification")
#         fun1()
#         print("After Modification")
#     return  inner_fun

# def fun():
#     print("this is from main function")    
# res=outer_fun(fun)
# res() 
    
# @outer_fun
# def fun():
#     print("This is From main function")
# fun()

# def fun(x,y,z):
#     return x+y+z

# res=outer_fun(fun)
# x=10
# y=20
# z=30
# res(x,y,z)
# fun(x,y,z)

# def outer_fun(fun1):
#     def inner_fun(r,s,t):
#         r=r+5
#         s=s+5
#         t=t+10
#         a=fun1(r,s,t)
#         print(t)
#     return inner_fun
# def fun(x,y,z):
#     return x+y+z
# res=outer_fun(fun)



