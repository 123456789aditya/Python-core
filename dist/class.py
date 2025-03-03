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

class Book:
    
    def welcome():
        print("welcome to my web page")
        
    @staticmethod
    def thanx():
        print("thanks for visit")
        
obj=Book()
Book.welcome()