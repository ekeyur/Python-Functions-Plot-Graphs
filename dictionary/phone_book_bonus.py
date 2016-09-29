import pickle


#open the file where the phone numbers will be saved in a write mode

myfile = open('phone_book_bonus.pickle','r')
phone_book = pickle.load(myfile)
# #phone_book = {'name':'111-111-1111'}



def savefile():
    raw = open('phone_book_bonus.pickle','w')
    pickle.dump(phone_book,raw)
    raw.close()


user_input = 0
while user_input != 6:
    print "\n"
    print "Electronic Phone Book"
    print "====================="
    print "1\. Look up an entry"
    print "2\. Set an entry"
    print "3\. Delete an entry"
    print "4\. List all entries"
    print "5\. Save entries"
    print "6\. Quit"

    user_input = int(raw_input("What do you want to do (1 - 6) >> "))

    if (user_input == 1):
        name = raw_input("Please enter person's name: ")
        for i,j in phone_book.items():
            if name == i:
                print j

    if (user_input == 2):
        name = raw_input("Please enter person's name: ")
        phone_book[name] = {}
        home1 = raw_input("Do you want to add a home number (Y or N) ").upper()
        if (home1 == 'Y'):
            home_number = raw_input("Enter Home Number ")
            phone_book[name]['home'] = home_number
        else:
            pass

        cell1 = raw_input("Do you want to add a Cell number (Y or N) ").upper()
        if (cell1 == 'Y'):
            cell_number = raw_input("Enter Cell Number ")
            phone_book[name]['cell'] = cell_number
        print "%s has been successfully added" % name


    if (user_input == 3):
        name = raw_input("Please enter person's name: ")
        if name in phone_book:
            del phone_book[name]
            print "%s has been successfully deleted from phone book" % name
        else:
            print "%s doesn't exist in the phone_book" % name

    if (user_input == 4):
        print phone_book

    if (user_input == 5):
        savefile()
        pass
    if (user_input == 6):
        pass
