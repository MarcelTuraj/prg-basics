class nums:
           def __init__(self):
                   self.box = []
           def add_nums(self):
                   user_input = input("Enter numbers")
                   while user_input.lower() != "exit" :
                           self.box.append(int(user_input))
                           user_input = input("Enter numbers (exit to finish.): ")
           def display(self):
                   string = ""
                   for i in range(len(self.box)):
                           string += f"{self.box[i]} "
                   print(string)
           def maxnum(self):
                   return max(self.box)
           def minnum(self):
                   return min(self.box)
           def mean(self):
                   return (sum(self.box))/len(self.box)
           def median(self):
                   sort_box = sorted(self.box)
                   if len(sort_box) % 2 == 0 :
                           return (sort_box[len(sort_box)/2] + sort_box[(len(sort_box)/2)-1])/2
                   else :
                           return sort_box[(len(sort_box)//2)+1]
           def displayinfo(self):
                   print(f"set: {self.box}")
                   print(f"max: {self.maxnum()}")
                   print(f"min: {self.minnum()}")
                   print(f"mean: {self.mean()}")
                   print(f"median: {self.median()}")
                

           
        
                   

        
