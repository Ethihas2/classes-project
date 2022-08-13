class BookStore:
    def __init__(self,name,author,price,time):
        self.book_name = name
        self.book_author = author
        self.price = price
        self.time = time
    def book_add(self):
        print("Book name: "+self.book_name)
        print("Book Author: "+self.book_author)
        print("Book Price: "+self.price)
        print("Book was published in: "+str(self.time))
        print("Book added")
        print("This book was published "+str(2022-self.time)+" ago")

book1 = BookStore("Wimpy Kid","Jeff Kinney","200",2010)
book1.book_add()
book2 = BookStore("Harry Potter", "J. K. Rowling", "1928", 1997)
book2.book_add()