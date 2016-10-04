import pickle
from os.path import exists

book = []
#open the file where the phone numbers will be saved in a write mode

class Entry(object):
    def __init__(this, name, cell,home):
        this.name = name
        this.cell = cell
        this.home = home

    def retrieve(this,name):
        print "%s cell # : %s" % (this.name,this.cell)
        print "%s home # : %s" % (this.name,this.home)


if exists('phone_book_class.pickle'):
    print 'Loading phone book.'
    myfile = open('phone_book_class.pickle','r')
    book = pickle.load(myfile)
    myfile.close()

else:

    book = []

def savefile(phone):
    # with open('phone_book_class.pickle','wb') as pf:
    #     pf.dump(obj,myfile)
    myfile = open('phone_book_class.pickle','w')
    pickle.dump(phone,myfile)
    myfile.close()
# class Contact(object):
#     def __init__(this, contact):
#         this.contact = Phonebook

user_input = 0

while user_input != 5:
    print "\n"
    print "Electronic Phone Book"
    print "====================="
    print "1\. Look up an entry"
    print "2\. Set an entry"
    print "3\. Delete an entry"
    print "4\. List all entries"
    print "5\. Quit"

    user_input = int(raw_input("What do you want to do? : "))

# Retrieve an entry
    if (user_input == 1):
        user = raw_input("Name? :")
        for entry in book:
            if entry.name == user:
                print "%s : home: %s, cell: %s" %(entry.name,entry.home,entry.cell)
# Add an entry
    if user_input == 2:
        name = raw_input("Please enter person's name: ")
        home = raw_input("Please enter person's home number: ")
        cell = raw_input("Please enter person's cell number: ")
        for entry in book:
            if not entry.name == name:
                entry = Entry(name,cell,home)
                book.append(entry)
        print "%s is saved" % name

    if user_input == 3:
        name = raw_input("Please enter person's name: ")
        for entry in book:
            if entry.name == name:
                book.pop(book.index(entry))
                print "%s has been successfully deleted from phone book" % name

    if (user_input == 4):
        for entry in book:
            print "%s : home: %s, cell: %s" %(entry.name,entry.home,entry.cell)

    if (user_input == 5):
        pass
    savefile(book)
