class book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
        self.is_borrowed=False
    def borrow(self):
        self.is_borrowed=True
        print("You have borrowed book",self.title)
    def return_book(self):
        self.is_borrowed=False
        print("Thank you for returning",self.title)

library=book("Harry potter","Jk sampson")
print(library.borrow())
print(library.return_book())




    
        