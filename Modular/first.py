# class Parent:
#     x=10
#     def car(self):
#         print("Parent Home")
        
# class Child(Parent):
#     y=20
#     def car(self):
#         super().car()
        
#         print("Child Car")
 
        
# obj=Child()
# print(obj.x)
# obj.car()












# class A:
#     def add(self,x,y,z):
#         print(x+y+z)
        
#     def add(self,x):
#         print(x)
        
#     def add(self,x,y):
#         print(x+y)
        
# obj=A()
# obj.add(3,5,)



# class Parent1:
#     def home(self):
#         print("parent1 home")
        
# class Parent2:
#     def home(self):
        
#         print("parent2 home")
        
# class Child(Parent1,Parent2):
#     def new(self):
        
#         print("child car")
        
# obj=Child()
# obj.home()







# class Grand_parent:
#     def home(self):
#         print("parent1 home")
        
# class Parent(Grand_parent):
#     def car(self):
#         print("parent2 car")
        
# class Child(Parent):
#     def new(self):
#         print("child new")
        
# obj=Child()
# obj.new()
# obj.car()
# obj.home()

# class Chasis:
#     def home(self):
#         print("car basic structure")
        
# class Engine(Chasis):
#     def engine(self):
#         print("car engine design")
        
# class Car(Engine):
#     def screen(self):
#         print("car price 500000")
        
# C1=Car()
# C1.home()
# C1.engine()




# class Human:
#     def __init__(self,name,age):
#         print("calling init from Human class")
#         self.name=name
#         self.age=age
        
#     def show(self):
#         print(f"name:{self.name}, age is:{self.age} ")
        
#     def eat(self):
#         print("I can eat")
        
# class Male(Human):
#     def __init__(self,name,age,location):
#         Human.__init__(self,name,age)
#         self.location=location
#         print(f"{self.name}{self.age}{self.location}")
        
#     def sleep(self):
#         print("i can slep whole day")
        
# class Female(Human):
    
#     def __init__(self,name,age,dance):
#         print("calling from female class")
#         super().__init__(name,age)
#         self.dance=dance
#         print(f"{self.name, self.age, self.dance}")
       
#     def work(self):
#         print("i can code")
        
# # f1=Female("sharon",21)
# # f1.show()
# # f1.eat()


# m1=Female("Sharon",21,"dance")
    
    
        
        





# a=lambda x,y : (x+y)
# p=10
# q=20
# print(a(p,q))


# n=int(input("enter any num"))
# check_num =lambda x:  'even no' if (x%2==0)  else 'odd'
# print(check_num(n))

# b=str(input("enter first password:"))
# c=str(input("enter passowrd again:"))

# res=lambda n,a: "passowrd matched" if n==a else "incorrect password"
# print(res(b,c))


# l1=[1,2,3,4,5,6,7,8,9,10]

# def display(x):
#     if x%2==0:
#         return x
    
        
# res=filter(display,l1)
# print(list(res))
    
# def even(x):
#     if x%2==0:
#         return 'even'
#     else:
#         return 'odd'
    
# l1=[1,20,30,0,40,50,60]
# res=filter(even,l1)
# print(list(res))


# def display(a):
#     if a>10:
#         return a
    
# l1=[1,2,3,10,20,30,40]
# res=filter(display,l1)
# print(list(res))


# l1=[1,2,3,4,5,6,6,7,9,10]
# x=filter(lambda a: a if a>3 else None,l1)
# print(list(x))

# l1=[1,2,3,4,5,6,7,8,9,10]
# print(list(filter(lambda a: a if a>3 else None,l1)))



# from functools import reduce
# def display(x,y):
#     return x+y
    
# l1=[1,2,3,4,5,6,7,8,9]
# res=reduce(display,l1)
# print(res)

# def div(a,b):
#     print(a/b)
    
# def smart(func):
#     def inner(a,b):
#         if a<b:
#             a,b=b,a
#         return func(a,b)
#     return inner

# div=smart(div)
# print(div(2,4))
    
      

    


# from functools import reduce

# def display(x,y):
#     return x+y

# my_list=[10,40,20,60,80,60]
# res=reduce(display,my_list)
# print(res)
    
    
    
    
    
    
    
    

# from functools import reduce

# def display(x,y):
#     return x+y

# my_list=[10,40,20,60,80,60]
# res=reduce(display,my_list)
# print(res)




# from functools import reduce

# def display(x,y):
#     return x+y

# my_list=[10,40,20,60,80,60]
# res=reduce(display,my_list)
# print(res)



from functools import reduce

def display(x,y):
    return x+y

my_list=[10,40,20,60,80,60]
res=reduce(display,my_list)
print(res)


# from functools import reduce

# def display(x,y):
#     return x+y

# my_list=[10,40,20,60,80,60]
# res=reduce(display,my_list)
# print(res)