import pickle
from os.path import exists

phone_book = []
#open the file where the phone numbers will be saved in a write mode
# if exists('phone_book_class.pickle'):
#     print 'Loading phone book.'
#     myfile = open('phone_book_class.pickle','rb')
#     # with open('phone_book_class.pickle','r') as pickled_file:
#     phone_book = pickle.load(myfile)
#     myfile.close()

def savefile(phone):
    myfile = open('phone_book_class.pickle','wb')
    for obj in phone_book:
        pickle.dump(obj,myfile)
    myfile.close()
# class Contact(object):
#     def __init__(this, contact):
#         this.contact = Phonebook

class Entry(object):
    def __init__(this, name, phones):
        this.name = name
        this.phone = phones



class Phone(object):
    def __init__(this, cell, home):
        this.cell = cell
        this.home = home

    def retrieve(this):
        print "%s cell # : %s" % (this.name,this.cell)
        print "%s home # : %s" % (this.name,this.home)

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
        # print phone_book
        #name = raw_input("Name : ")
        for n in range(len(phone_book)):
            print n

# Add an entry
    if user_input == 2:
        name = raw_input("Please enter person's name: ")
        home = raw_input("Please enter person's home number: ")
        cell = raw_input("Please enter person's cell number: ")

        phone = Phone(home,cell)
        entry = Entry(name,phone)
        phone_book.append(entry)

        print "%s is saved" % name
        pass

savefile(entry)




    # if (user_input == 3):
    #     name = raw_input("Please enter person's name: ")
    #     if name in phone_book:
    #         del phone_book[name]
    #         print "%s has been successfully deleted from phone book" % name
    #     else:
    #         print "%s doesn't exist in the phone_book" % name
    #
    # if (user_input == 4):
    #     print phone_book
    #
    # if (user_input == 5):
    #     savefile()
    #     pass
    # if (user_input == 6):
    #     pass
