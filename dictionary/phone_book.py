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
    #print "6\. Quit"

    user_input = int(raw_input("What do you want to do (1 - 5) >> "))

    if (user_input == 1):
        name = raw_input("Name : ")
        if name in phone_book:
            print "%s : %s" % (name,phone_book.get(name))
        else:
            print "%s doesn't exist in the phone_book" % name

    if (user_input == 2):
        name = raw_input("Name : ")
        number = raw_input("Number (xxx-xxx-xxxx): ")
        phone_book[name] = number
        savefile(name,number)
        # Writing the information to the phone_book.pickle file
    if (user_input == 3):
        name = raw_input("Name : ")
        if name in phone_book:
            del phone_book[name]
            print "%s has been successfully deleted from phone book" % name
        else:
            print "%s doesn't exist in the phone_book" % name

    if (user_input == 4):
        print phone_book

    if (user_input == 5):
        print "Bye"
        break

    # if (user_input == 6):
    #     pass
