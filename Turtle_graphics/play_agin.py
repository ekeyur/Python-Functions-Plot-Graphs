def play_again():
    user = raw_input("Do you want to play again (Y or N): ").upper()
    if user == 'Y':
        return True
    elif user == 'N':
        return False
    else:
        print "Invalid Input"
        play_again()

print play_again()
