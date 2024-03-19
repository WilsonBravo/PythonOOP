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
    
    # return json contact list
    def to_json_list(self, contactList):

        jsonContactList=[]

        for contact in contactList:
            jsonContactList.append(contact.to_json())

        return jsonContactList

    # add contact
    def add(self, firstName, lastName, phoneNumber, email):
        self.contactList.append(contact(firstName, lastName, phoneNumber, email, self.contactId))
        self.contactId+=1

        return f"You added the following contact:\n{json.dumps(contact(firstName, lastName, phoneNumber, email, self.contactId).to_json(), indent=2)}"

    # delete contact
    def delete(self, firstName=None, lastName=None, phoneNumber=None, email=None):
        if not firstName and not lastName and not phoneNumber and not email:
            return "Enter data before calling the method"
        
        contacts_to_delete = []

        for contact in self.contactList:
            if (firstName is None or contact.firstName == firstName) and \
            (lastName is None or contact.lastName == lastName) and \
            (phoneNumber is None or contact.phoneNumber == phoneNumber) and \
            (email is None or contact.email == email):
                contacts_to_delete.append(contact)
        
        if contacts_to_delete:
            for contact in contacts_to_delete:
                self.contactList.remove(contact)

            contacts_to_delete=self.to_json_list(contacts_to_delete)

            return f"The following contacts were deleted:\n{json.dumps(contacts_to_delete, indent=2)}"
        else:
            return "There are no contacts to delete"
    
    # search contact
    def search(self, firstName=None, lastName=None, phoneNumber=None, email=None):
        if not firstName and not lastName and not phoneNumber and not email:
            return "Enter data before calling the method"
        
        contacts_found = []

        for contact in self.contactList:
            if (firstName is None or contact.firstName == firstName) and \
            (lastName is None or contact.lastName == lastName) and \
            (phoneNumber is None or contact.phoneNumber == phoneNumber) and \
            (email is None or contact.email == email):
                contacts_found.append(contact)
        
        if contacts_found:
            contacts_found=self.to_json_list(contacts_found)

            return f"The following contacts were found:\n{json.dumps(contacts_found, indent=2)}"
        else:
            return "No contacts found"

    # show contact
    def show(self):
        if self.contactList:
            jsonContactList=self.to_json_list(self.contactList)
            return (f"Your contacts are:\n{json.dumps(jsonContactList, indent=2)}")
        else:
            return "You have no contacts"
