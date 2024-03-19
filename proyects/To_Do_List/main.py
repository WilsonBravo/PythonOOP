class task:
    def __init__(self, description, startDate, dueDate, status):
        self.description = description
        self.startDate = startDate
        self.dueDate = dueDate
        self.status = status

    def to_json(self):
        return {
            "id": self.id,
            "firstName": self.firstName,
            "lastName": self.lastName,
            "phoneNumber": self.phoneNumber,
            "email": self.email
        }

class toDoList:
    def __init__(self):
        pass

    # return json contact list
    def to_json_list(self, contactList):

        jsonContactList=[]

        for contact in contactList:
            jsonContactList.append(contact.to_json())

        return jsonContactList

    def add(self):
        pass

    def delete(self):
        pass

    def updateStatus(self):
        pass

    def show(self):
        pass