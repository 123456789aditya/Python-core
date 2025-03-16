# class Book:
#     price=100
#     total_pages=70
#     def __init__(self,title,author):
#         self.title=title
#         self.author=author
        
#     @classmethod
#     def update(cls,new_price,new_page_count):
#         cls.price=new_price
#         cls.total_pages=new_page_count
        
#     @classmethod
#     def add_new(cls,author):
#         cls.author=author
        
#     def show_details(self):
#         print(self.title,self.author,Book.price,Book.total_pages)
        
# obj=Book('python','neeraj')
# Book.update(110,550)
# obj.show_details()


#staticmethod


# class Book:
    
#     def welcome():
#         print("welcome to my web page")
        
#     @staticmethod
#     def thanx():
#         print("thanks for visit")
        
# obj=Book()
# Book.welcome()


# from abc import ABC,abstractmethod

# class BankApp(ABC):
#     def login(self):
#         print("user login")
    
#     def logout(self):
#         print("user logout")
        
#     def userdetail(self):
#         print("user details")
        
#     @abstractmethod
    
#     def database(self):
#         pass
    
# class WebPage(BankApp):
#     def database(self):
#         print("database connected")
        
        
# obj=WebPage()
# obj.login()
# obj.logout()
# obj.userdetail()

#Inheritance............

# class A:
#     x=10
#     y=20
#     def home(self):
#         print("have a home")
        
#     def car(self):
#         print("have a car")
        
# class B(A):
#     def newHome(self):
#         print("new home")
        
# obj=B()
# obj.home()

#Types of Inheritance 
#single,multiple,multilevel ,hirarichial inheritance

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

#if 2 metyhods in p-c class have same name then it is called as functioon overriding..


# class A:
#     def add(self,x,y,z):
#         print(x+y+z)
        
#     def add(self,x):
#         print(x)
        
#     def add(self,x,y):
#         print(x+y)
        
# obj=A()
# obj.add(2,3)


#multiple inheritance...child class usses MRO technique

# class Parent1:
#     def home(self):
#         print("parent1 home")
        
# class Parent2:
#     def home(self):
#         print("parent2 home")
        
# class Child(Parent2,Parent1):
#     def car(self):
#         print("child car")
        
# obj=Child()
# obj.home()

#Multilevel inheritance

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

#hierarical inheritance

# class Parent:
#     def home(self):
#         print("from parent class")
    
# class Child1(Parent):
#     def home(self):
#         #print("from child1 class")
#         super().home()
        
# class Child2(Parent):
#     def home(self):
#         print("from child2 class")
        
# obj=Child1()
# obj.home()
# obj=Child2()
# obj.home()

#Hybrid inheritance#################



# class Parent:
#     def home(self):
#         print("from parent class")
    
# class Child1(Parent):
#     def home(self):
#         print("from child1 class")
#         super().home()
        
# class Child2(Parent):
#     def home(self):
#         print("from child2 class")      
        
class Child3(Child1,Child2):
    def new(self):
        print("from child3")
        
obj=Child3()
obj.home()
print(Child3.__mro__)  




