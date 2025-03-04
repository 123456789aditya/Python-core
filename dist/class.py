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



class A:
    x=10
    y=20
    def home(self):
        print("have a home")
        
    def car(self):
        print("have a car")
        
class B(A):
    def newHome(self):
        print("new home")
        
obj=B()
obj.home()