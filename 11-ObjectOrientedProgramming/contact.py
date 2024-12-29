class Contact:
    def __init__(self, name, email, telephone):
        self.name = name
        self.email = email 
        self.telephone = telephone
    def store(self):
        cont = {"name": self.name,
                "email": self.email,
                "telephone": self.telephone

        }
        return cont
        
    