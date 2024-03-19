import json

class contact:
    def __init__(self, firstName, lastName, phoneNumber, email, id):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.phoneNumber = phoneNumber
        self.email = email

    def to_json(self):
        return {
            "id": self.id,
            "firstName": self.firstName,
            "lastName": self.lastName,
            "phoneNumber": self.phoneNumber,
            "email": self.email
        }

class contactListClass:
    def __init__(self):
        self.contactId=0
        self.contactList=[]

    # add contact
    def add(self, firstName, lastName, phoneNumber, email):
        self.contactList.append(contact(firstName, lastName, phoneNumber, email, self.contactId))
        self.contactId+=1

    # delete contact
    # search contact
    # show contact
    def show(self):
        jsonContactList=[]

        for contact in self.contactList:
            jsonContactList.append(contact.to_json())

        print(json.dumps(jsonContactList, indent=2))
