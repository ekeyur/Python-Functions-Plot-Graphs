import pickle
from os.path import exists


#open the file where the phone numbers will be saved in a write mode
if exists('phone_book.pickle'):
    print 'Loading phone book.'
    myfile = open('phone_book.pickle','r')
    phone_book = pickle.load(myfile)
else:
    phone_book = {}

def savefile(name,number):
    myfile = open('phone_book.pickle','w')
    pickle.dump(phone_book,myfile)
    myfile.close()
    print "%s : %s has been successfully added" % (name,number)


class Contact(object):
    def __init__(this, contact):
        this.contact = Phonebook

class Phonebook(object):
    def __init__(this, name , email, phone):
        this.name = name
        this.email = email
        this.phone = Phone

class Phone(object):
    def __init__(this, cell, home):
        this.cell = cell
        this.home = home



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

    
