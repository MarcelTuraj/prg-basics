class C:
    def __init__(self, coordslist):
        self.coordslist = coordslist
    def m(self, n):
        counter = 0
        for item in self.coordslist:
            if item[0] > 0 and item[1] > 0:
                counter += 1
        if counter >= n:
            return True
        else :
            return False
        