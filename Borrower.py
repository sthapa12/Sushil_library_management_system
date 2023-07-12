import csv


 
class Member():
    
    
    def __init__(self, name, email, address, city, zip_code, membership_id):
        self.name = name
        self.email = email
        self.address = address
        self.city = city
        self.zip_code = zip_code
        self.membership_id = membership_id

    def add_member(self):
        member_data =f"{self.name},{self.email},{self.address},{self.city},{self.zip_code},{self.membership_id}\n"
        found = self.search_member_by_membership_id(self.membership_id)
        print('--------------------')
        print(self.membership_id)
        print('--------------------')
        if not found:
            with open("member_data.csv", "a") as file:
                file.write(member_data)
            print('--------------------')
            print("Member added successfully!")
            print('--------------------')
        else:
            print('--------------------')
            print("Member already exists!")
            print('--------------------')

    def search_member_by_membership_id(self, membership_id):
        found = False
        with open("member_data.csv", "r") as file:
            for line in file:
                member_info = line.strip().split("---")
                print('--------------------------')
                print(member_info)
                print('--------------------------')
                print(member_info[-1])
                if member_info[-1] == membership_id:
                    found = True
                    return found
            if not found:
                return found
            
    def update_member(self):
        member_data = f"{self.name},{self.email},{self.address},{self.city},{self.zip_code},{self.membership_id}\n"
        found = self.search_member_by_membership_id(self.membership_id)
    
        if found:
            updated_data = []
            with open("member_data.csv", "r") as file:
                for line in file:
                    member_info = line.strip().split(",")
                    if member_info[-1] == self.membership_id:
                    # Update the member's information
                        member_info[0] = self.name
                        member_info[1] = self.email
                        member_info[2] = self.address
                        member_info[3] = self.city
                        member_info[4] = self.zip_code

                    updated_data.append(",".join(member_info))
        
            # Write the updated data back to the file
            with open("member_data.csv", "w") as file:
                file.write("\n".join(updated_data))

            print("Member updated successfully!")
        else:
            print("Member not found.")
         
            
            
            
            
    # def update_member(self):
    #     member_data = f"{self.name},{self.email},{self.address},{self.city},{self.zip_code},{self.membership_id}\n"
    #     found = self.search_member_by_membership_id(self.membership_id)
    #     if found:
    #         with open("member_data.csv", "w+") as file:
    #            file.write(member_data)
               
    #         for updated_borrower in file:
    #             name = name
    #             email=email
    #             address=address
    #             city=city
    #             zip_code=zip_code
                
    #             member_data=member_data

    #     print('--------------------')
    #     print("Member updated successfully!")
    #     print('--------------------')
        
        return member_data
