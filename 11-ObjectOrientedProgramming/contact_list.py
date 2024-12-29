from contact import Contact
class Contact_list:
    def __init__(self):
        self.container = []
    def adjustment(self, name, email, telephone):
        contact = Contact(name, email, telephone)
        data = contact.store()
        self.container.append(data)

    
    
    def display(self):
        for item in self.container:
            print(f"name: {item["name"]}, email: {item["email"]}, tel: {item["telephone"]}")

    

    