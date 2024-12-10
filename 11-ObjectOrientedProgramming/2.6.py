class Phone: 
    def __init__(self, brand, model, battery_condition):
        self.brand = brand
        self.model = model
        self.battery_condition = battery_condition
        self.isturnedon = False
        self.current_app = ""
        self.state_of_battery = ""

    def is_battery_good(self, battery_condition):
        if self.battery_condition >= 50:
            self.state_of_battery = "good condition"
            
        else :
            self.state_of_battery = "bad condition of the battery"
    def turn_on(self):
        self.isturnedon = True
    def open_youtube(self):
        self.current_app = "Youtube"
    def display_info(self):
        print("PHONE INFO")
        print(f"brand: {self.brand}")
        print(f"model: {self.model}")
        print(f"battery condition: {self.battery_condition}%")
        print(f"State of the battery: {self.state_of_battery}")
        print(f"Phone is turned on: {self.isturnedon}")
        print(f"current app: {self.current_app}")


def main():
    phone = Phone("Iphone", "13 PRO", 88)
    phone.turn_on()
    phone.open_youtube()
    phone.is_battery_good(88)
    phone.display_info()

if __name__ == "__main__":
    main()

    
