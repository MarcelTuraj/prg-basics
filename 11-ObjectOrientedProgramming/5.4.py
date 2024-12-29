from ebook import Ebook
def main():
    myebook = Ebook("Niggaz", "Jan Borkowski", 256)
    myebook.openbook()
    myebook.show_info()
    myebook.set_page(256)
    myebook.reader()
    myebook.next()
    myebook.reader()
    myebook.set_page(13)
    myebook.reader()
    myebook.previous()
    myebook.reader()
    myebook.show_info()
    myebook.closebook()
    myebook.reader()

if __name__ == "__main__":
    main()