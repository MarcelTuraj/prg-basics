class C   :
    def __init__(self, counter):
        self.counter = counter
    def m1(self):
        print(self.counter)
    def m2(self):
        self.counter += 1
    def m3(self):
        self.counter -= 1
    def m4(self, n):
        self.counter += n
    def __str__(self):
        print(f"{self.counter}")
        
def main():
    c=C(5) 
    c.m1() 
    c.m2() 
    c.m1() 
    c.m4(-8) 
    c.m1() 
    c.m3() 
    c.m1() 
    c.m4(10) 
    c.m1() 
    c.__str__()

if __name__ == "__main__":
    main()