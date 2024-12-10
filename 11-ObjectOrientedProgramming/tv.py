class Television:
    def __init__(self, is_on):
        self.is_on = False
    def turn_on(self):
        self.is_on = True
    def turn_off(self):
        self.is_on = False
    def show_status(self):
        if self.is_on == True:
            print("TV is turned on")
        else :
            print("TV is turned off")
    
    
    
    