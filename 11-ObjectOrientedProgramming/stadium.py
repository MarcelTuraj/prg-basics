class C:
    def __init__(self, data):
        self.data = data
    def m1(self, s, n):
        self.data[s] = n
    def display_data(self):
        for key, value in self.data.items():
            print(f"key: {key}  value: {value}")
    def m2(self, s):
        suma = 0
        for char in s:
            if char in self.data.keys():
                suma += self.data[char]
            
        return suma
    



        
