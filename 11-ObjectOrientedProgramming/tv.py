class Television:
    def __init__(self):
        self.is_on = False
        self.channels_list = []
        self.channel_no = 1
        self.volume = 0
    def turn_on(self):
        self.is_on = True
    def turn_off(self):
        self.is_on = False
    def show_status(self):
        if self.is_on == True:
            print("TV is turned on")
            print("Current volume: ", self.volume)
            if len(self.channels_list) != 0 and not len(self.channels_list) < self.channel_no:
                
                print(f"{self.channel_no} ({self.channels_list[self.channel_no - 1]})")
            else :
                raise ValueError(f"There is no channel {self.channel_no} in program.")
            


        else :
            print("TV is turned off")
    def add_channels(self):
        user_input = input("Enter a value to append to the array (or 'exit' to stop): ")
        while user_input.lower() != 'exit':
            # Append the user input to the array
            self.channels_list.append(user_input)
            # Get the next input
            user_input = input("Enter a value to append to the array (or 'exit' to stop): ")

    def set_channel(self, new_channel_no):
        self.channel_no = new_channel_no
        
        
    def show_channels(self):
        for i in range(0, len(self.channels_list)):
            print(f"{i+1}.",self.channels_list[i])
    def increase_volume(self):
        if not self.volume == 10:
           self.volume += 1
        else : 
            print("Can't go above 10")
    def decrease_volume(self):
        if not self.volume == 0:
            self.volume -= 1
        else:
            print("Can't go below zero.")
            
    
    
    
    