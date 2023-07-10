class Library:
    
    def __init__(self, total_books, name, address, rules):
        self.total_books = total_books
        self.name = name
        self.address = address
        self.rules = rules

class Book():
    def __init__(self, book.id, name, title, author_name, quantity, pub_year, edition):
        self.book.id = book.id
        self.name = name
        self.title = title
        self.author_name = author_name
        self.quantity = quantity
        self.pub_year = pub_year
        self.edition = edition

class CrimeTrhilerBook(Book):
    def __init__(self, book_id, name, title, author_name, pub_year, edition, is_part_of_series, crime_triller_rating):
        super().__init__(name=name, book_id=book_id, title=title, author_name=author_name, edition=edition, quantity=quantity, pub_year=pub_year)
        self.is_part_of_series = is_part_of_series
        self.crime_triller_rating = crime_triller_rating

class RomanNovel(Book):
    
    def __init__(self, book_id, name, title, author_name, quantity, pub_year, edition, is_it_classic):
        super().__init__(book_id, name, title, author_name, quantity, pub_year, edition)
        self.is_it_classic = is_it_classic
        
class Borrower:
    def __init__(self,user_name, member_id, phone):
        self.user_name=user_name
        self.phone=phone