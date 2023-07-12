from books import Book
from Borrower import Member
def selection_validate():
 
 
    valid_selections = ('1', '2', '3', '4', '5', '6')
    message = input("Welcome to the main menu. Press enter to continue: ")
    loop = 'yes'
    while True and loop == 'yes':
        selection = input("\nPlease select from the following menu (Type exit to exit program) \n"
                          "To request a new loan enter 1 \n"
                          "To return a book enter 2 \n"
                          "To extend a loan enter 3 \n"
                          "To add a user enter 4 \n"
                          "To update a user enter 5 \n"
                          "To add a book enter 6 \n"
                          "\nEnter choice: ")

        if selection == 'exit':
            break
        else:
            if selection in valid_selections:
                loop = 'no'
            else:
                print('\nValue: {} did not match any menu choice'.format(selection))
                loop = 'yes'
    return selection

def selection_calls():
    selection = selection_validate()
    if selection == '1':
        pass
    elif selection == '2':
        pass
    elif selection == '3':
        pass
    elif selection == '4':
        name = input("Enter Member Name: ")
        email = input("Enter Member Email: ")
        address = input("Enter Member Email: ")
        city = input("Enter Member city: ")
        zip_code = input("Enter Member Zip-Code: ")
        membership_id = input("Enter Membership ID: ")
        
        new_member = Member(name=name, email=email, address=address, city=city, zip_code=zip_code, membership_id=membership_id)
        new_member.add_member()
    
    elif selection == '5':
        membership_id = input("Enter Membership ID: ")
        member_update = Member(None, None, None, None, None, None)
        found = member_update.search_member_by_membership_id(membership_id)
        if found:
            print("Member found. ")
            name = input("Enter new user name: ")
            email = input("Enter Member Email: ")
            address = input("Enter Member Address: ")
            city = input("Enter Member City: ")
            zip_code = input("Enter Member Zip-Code: ")
            updated_member = Member(name, email, address, city, zip_code, membership_id)
            updated_member.update_member()
        else:
            print("Member not found.")     
         
        
        # if found: 
        #     print("Member found. ")
        #     name = input("Enter Member's New name: ")
        #     email = input("Enter Member's New Email: ")
        #     address = input("Enter Member's New Email: ")
        #     city = input("Enter Member's New city: ")
        #     zip_code = input("Enter Member Zip-Code: ")
        #     membership_id = input("Enter Membership ID: ")
        # else:
        #     new_member = Member(name=name, email=email, address=address, city=city, zip_code=zip_code, membership_id=membership_id)
        #     new_member.update_member()

# user_name, email, address, city, zip_code, membership_id

    elif selection == '6':
        book_name = input("Enter Book Name: ")
        title = input("Enter Title: ")
        author_name = input("Enter author: ")
        quantity = input("Enter quantity: ")
        pub_year = input("Enter Publication Year: ")
        edition = input("Enter Edition: ")
        book_id = input("Enter Book Id: ")
        
        new_book = Book(book_id=book_id, book_name=book_name, title=title, author_name=author_name, quantity=quantity, pub_year=pub_year, edition=edition)
        new_book.add_book()

if __name__ == '__main__':
    selection_calls()