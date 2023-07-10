import csv



class Book():
    
    def __init__(self, book_id, book_name, title, author_name, quantity, pub_year, edition):
        self.book_id = book_id
        self.book_name = book_name
        self.title = title
        self.author_name = author_name
        self.quantity = quantity
        self.pub_year = pub_year
        self.edition = edition
        
    def add_book(self):
        book_data = f"{self.book_id},{self.book_name},{self.title},{self.author_name},{self.quantity},{self.edition},{self.pub_year}\n"
        found = self.search_book_by_title(self.title)
        print('--------------------------')
        print(self.title)
        print('--------------------------')
        if not found:
            with open("book_data.csv", "a") as file:
                file.write(book_data)
            print('--------------------')
            print("Book added successfully!")
            print('--------------------')
        else:
            print('--------------------')
            print("Book already exist")
            print('--------------------')
    
    def search_book_by_title(self, title):              
        found = False
        with open("book_data.csv", "r") as file:
            for line in file:
                book_info = line.strip().split(",")
                print('--------------------------')
                print(book_info)
                print('--------------------------')
                print(book_info[3])
                if book_info[3] == title:
                    found = True
                    return found
            if not found:
                return found
            
    def search_book_by_author(self, author_name):              
        found = False
        with open("book_data.csv", "r") as file:
            for line in file:
                book_info = line.strip().split(",")
                print('--------------------------')
                print(book_info)
                print('--------------------------')
                print(book_info[4])
                if book_info[4] == author_name:
                    found = True
                    return found


            if not found:
                return found