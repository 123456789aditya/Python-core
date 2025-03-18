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

class Chasis:
    def home(self):
        print("car basic structure")
        
class Engine(Chasis):
    def engine(self):
        print("car engine design")
        
class Car(Engine):
    def screen(self):
        print("car price 500000")
        
C1=Car()
C1.home()
C1.engine()
