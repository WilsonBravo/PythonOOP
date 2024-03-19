def contactManagerTest(contactListClass, contacts):
    print("*"*60,"\nContact Manager Test\n")
    contactList = contactListClass()
    for contact in contacts:
        print(">>\n",contactList.add(contact["first name"], contact["last name"], contact["phone number"], contact["email"]))

    print(">>\n",contactList.delete(firstName="Juan"))
    print(">>\n",contactList.show())
    print(">>\n",contactList.search(firstName="Dennis"))