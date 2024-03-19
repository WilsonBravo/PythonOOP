def contactManagerTest(contactListClass, contacts):
    contactList = contactListClass()
    for contact in contacts:
        contactList.add(contact["first name"], contact["last name"], contact["phone number"], contact["email"])

    contactList.show()