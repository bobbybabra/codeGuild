dictionary = {
    'chris': {'name': 'Chris', 'phone': "503-277-9710"},
    'sam': {'name': 'Sam', 'phone': "503-277-9710"}
}


def search():
    try:
        srch = raw_input("Please enter the first name of the person you are searching for: ").lower()
        print "Name: " + dictionary[srch]['name']
        print "Phone Number: " + dictionary[srch]['phone']
    except KeyError:
        print "Entry not found."


def add():
    name = raw_input("What is the first name of the person you wish to add?: ")
    phone = raw_input("What is the phone number of the person you wish to add?: ")
    dictionary[name.lower()] = {'name': name, 'phone': phone}
    print "Entry added:"
    print "Name: " + dictionary[name.lower()]['name']
    print "Phone Number: " + dictionary[name.lower()]['phone']


def change():
    name = raw_input("What is the first name of the person you wish to change?: ")
    print "Do you: really want to change %s?" % name
    print"Yes or No"
    running = True
    while running:
        try:
            choice = raw_input('> ').lower()
            if choice == "yes" or choice == "y":
                name_change = raw_input("What is the new name for %s: " % name)
                phone = raw_input("What is the new phone number for %s: " % name)
                dictionary[name_change.lower()] = {'name': name_change, 'phone': phone}
                dictionary.pop(name.lower())
                running = False
            if choice == "no" or choice == "n":
                running = False
        except ValueError:
            print "That is not a valid entry. Please try again."


def remove():
    name = raw_input("What is the first name of the person you wish to remove?: ")
    print "Are you sure you wish to remove %s?" % name
    print "Yes or No."
    running = True
    while running:
        try:
            choice = raw_input('> ').lower()
            if choice == "yes" or choice == "y":
                dictionary.pop(name.lower())
                print "%s has been removed." % name
                running = False
            if choice == "no" or choice == "n":
                running = False
        except ValueError:
            print "That is not a valid entry. Please try again."


def phone_book():
    print "Welcome to the Phone Book!"
    while True:
        print "-" * 40
        print "Press 1 to search."
        print "Press 2 to add."
        print "Press 3 to change an entry."
        print "Press 4 to remove."
        print "Press 5 to exit."
        print "-" * 40
        try:
            choice = int(raw_input('> '))
            if choice == 1:
                search()
            if choice == 2:
                add()
            if choice == 3:
                change()
            if choice == 4:
                remove()
            if choice == 5:
                exit()
        except ValueError:
            print "That is not a valid entry. Please try again."

phone_book()
