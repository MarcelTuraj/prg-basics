import random
class Thermo:
    def __init__(self):
        self.ison = False
        self.measurement = 0
    def turnon(self):
        if self.ison == False :
            self.ison = True
            print("Thermo has been turned on. ")
        else :
            print("Already on. ")
    def turnoff(self):
        if self.ison == True:
            self.ison = False
            print("Thermo has been turned off. ")

        else :
            print("Already off. ")

    def measure(self):
        if self.ison == False:
            print("Thermo off")
        else :
            self.measurement = round((random.uniform(34.0,42.0)),1)
    def display(self):
        if self.ison == False:
            print("Thermo: off")
        else:
            if self.measurement >= 37.0 and self.measurement < 41.0:
                print(f"Temperature: {self.measurement} (fever)")
            elif self.measurement >= 41.0 :
                print(f"Temperature: {self.measurement}")
                print("CRITICAL TEMPERATURE!!!111")
            elif self.measurement < 37.0 or self.measurement < 41.0 :
                print(f"Temperature: {self.measurement}")
            
    
