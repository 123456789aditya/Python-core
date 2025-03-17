# # def add(x,y,z):
# #     return x+y+z

# # def display():
# #     print("hi")

# from abc import ABC,abstractmethod

# class Computer(ABC):
#     @abstractmethod
#     def process(self):
#         pass

# class Laptop():
#     def one(self):
#         print("its running")
        
        
# class Program(Computer):
#     def process(self,com):
#         print("Solving Bugs")
        
        
        
# com=Computer()        
# p1=Program()
# p1.process()

from abc import ABC,abstractmethod

class BankApp(ABC):
    def login(self):
        print("user login")
    
    def logout(self):
        print("user logout")
        
    def userdetail(self):
        print("user details")
        
    @abstractmethod
    
    def database(self):
        pass
    
class WebPage(BankApp):
    def database(self):
        print("database connected")
        
        
obj=WebPage()
obj.login()
obj.logout()
obj.userdetail()
obj.database()