class C:
    def __init__(self, name, lastname, age, seniority):
        self.name = str(name)
        self.lastname = str(lastname)
        self.age = int(age)
        self.seniority = str(seniority)
    def __str__(self):
        if self.age >= 18:
            return f"{self.lastname.upper()}{self.name[0].upper()}{self.seniority}"
        else :
            return f"{self.lastname.lower()}{self.name[0].lower()}{self.seniority}"
         
        