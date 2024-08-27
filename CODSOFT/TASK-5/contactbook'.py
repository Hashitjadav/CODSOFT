from beautifultable import BeautifulTable

class Contact_Book:
    def __init__(self):
        self.__data = {}

    def Add_contact(self, name=None, address=None, email=None, phone=None):
        if name and address and email and phone:
            if phone not in self.__data:
                self.__data[phone] = [name, address, email, phone]
                print("Added contact")
            else:
                print("Contact already exists")
        else:
            print("Enter all fields to add")

    def Delete_contact(self, phone=None):
        if phone:
            if phone in self.__data:
                del self.__data[phone]
                print("Deleted contact")
            else:
                print("Contact does not exist")
        else:
            print("Enter phone number to delete")

    def Update_contact(self, phone=None, name=None, address=None, email=None):
        if phone and phone in self.__data:
            lst_info = self.__data[phone]
            if name:
                lst_info[0] = name
            if address:
                lst_info[1] = address
            if email:
                lst_info[2] = email
            self.__data[phone] = lst_info
            print("Updated contact")
        else:
            print("Contact does not exist")

    def Search_contact(self, query=None):
        if query:
            search_arr = []
            for key, val in self.__data.items():
                search_arr.append(val + [" ".join(val)])
                
            result = set()
            for word in query.split():
                for i in range(len(search_arr)):
                    if word in search_arr[i][-1]:
                        result.add(i)
            
            ans = [search_arr[i][:-1] for i in result]
            return ans  
        else:
            return []

    def Display_all_contacts(self, data=None):
        if data is None:
            data = self.__data.values()
        
        table = BeautifulTable()
        for child_data in data:
            table.rows.append(child_data)
        
        table.rows.header = [str(i) for i in range(1, len(data) + 1)]
        table.columns.header = ["Name", "Address", "Email", "Phone"]
        print(table)

    def console(self):
        while True:
            try:
                choice = int(input("\nChoose an option:\n1. Add contact\n2. Delete contact\n3. Update contact\n4. Search contact\n5. Display all contacts\n6. Exit\n"))
                if choice == 1:
                    name = input("Enter name: ")
                    address = input("Enter address: ")
                    email = input("Enter email: ")
                    phone = input("Enter phone: ")
                    self.Add_contact(name, address, email, phone)

                elif choice == 2:
                    phone = input("Enter phone: ")
                    self.Delete_contact(phone)

                elif choice == 3:
                    phone = input("Enter phone: ")
                    name = input("Enter name: ")
                    address = input("Enter address: ")
                    email = input("Enter email: ")
                    self.Update_contact(phone, name, address, email)

                elif choice == 4:
                    query = input("Search: ")
                    result = self.Search_contact(query)
                    self.Display_all_contacts(result)

                elif choice == 5:
                    data = list(self.__data.values())
                    self.Display_all_contacts(data)

                elif choice == 6:
                    break

            except Exception as e:
                print("An error occurred:", e)

Contact_Book().console()
