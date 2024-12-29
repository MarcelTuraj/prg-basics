from contact import Contact
from contact_list import Contact_list
def main():
    
    list = Contact_list()
    list.adjustment("John Brown","brown@onet.pl","555234000")
    list.adjustment("Anna May", "am@o2.pl","232000199")
    list.adjustment("George Small","smallg@google.pl","222999100")
    list.display()

    
    
    
if __name__ == "__main__":
    main()