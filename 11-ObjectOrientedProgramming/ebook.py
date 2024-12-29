class Ebook():
    def __init__(self, title, author, pagenum):
        self.title = title
        self.author = author
        self.pagenum = pagenum
        self.isopen = False
        self.currentpage = 0
    def openbook(self):
        if self.isopen == False:
            self.isopen = True
        else : 
            print("Already open. ")
    def closebook(self):
        if self.isopen == True:
            self.isopen = False
        else:
            print("Already closed. ")
    def set_page(self, page):
        if self.isopen == False:
            print("First open the book")
        else :
            
             if not page <= 0 and not page > self.pagenum:
                self.currentpage = page
             else :
               print("No such page")
    def next(self):
        if self.isopen  :
           if not self.currentpage == self.pagenum:
                self.currentpage += 1
           else :
               print("Impossible. ")
        else :
            print("first open the book")
    def previous(self):
        if self.isopen:
    
           if not self.currentpage == 0 :
             self.currentpage -= 1
           else :
               print("Impossible. ")
        else :
            print("First open the book. ")
    def reader(self):
        if self.isopen:
            print(f"Currently displaying page {self.currentpage}")
        else :
            print("Book is closed. ")
    def show_info(self):
        if self.isopen:

            print(f"{self.title}, {self.author}, {self.pagenum}, {self.currentpage}, {self.isopen}")
        else :
            print(f"{self.title}, {self.author}, {self.pagenum}, {self.isopen}")
    

    
