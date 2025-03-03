# def even(x):
#     if x%2==0:
#         return 'even'
#     else:
#         return 'odd'
    
# l1=[1,20,30,0,40,50,60]
# res=filter(even,l1)
# print(list(res))


#reduce............

from functools import reduce
def display(x,y):
    return x+y
    
l1=[1,2,3,4,5,6,7,8,9]
res=reduce(display,l1)
print(res)



