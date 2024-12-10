# class definition
class Student():
    def __init__(self):
        self.name = ""
        self.age = 0
        self.program_name = ""

def main():
    # object creation based on the class
    student1 = Student()
    student2 = Student()
    student3 = Student()
    student1.name = "Dominic"
    student1.age = 19
    student1.program_name = "Finanse i Rachunkowość"
    student2.name = "Olivia"
    student2.age = 21
    student2.program_name = "Informatyka Stosowana"
    student3.age = 20
    student3.name = "Marcin"
    student3.program_name = "Analityka Gospodarcza"

    print('LIST OF STUDENTS')
    print('================')
    print(f'{student1.name}, {student1.age} years old, program : {student1.program_name}')
    print(f'{student2.name}, {student2.age} years old, program: {student2.program_name}')
    print(f"{student3.name}, {student3.age} years old, program: {student3.program_name}")

if __name__ == "__main__":
    main()