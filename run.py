import proyects
import test

contacts = [
    {
        "first name": "Wilson", 
        "last name": "Bravo", 
        "phone number": "1234567890", 
        "email": "wilson@email.com"
    },
    {
        "first name": "Dennis", 
        "last name": "Ballen", 
        "phone number": "1234567890", 
        "email": "dennis@email.com"
    },
    {
        "first name": "Juan", 
        "last name": "Acosta", 
        "phone number": "1234567890", 
        "email": "juan@email.com"
    }
]

test.calculatorTest(proyects.calculator, 1, 0)
test.contactManagerTest(proyects.contactListClass, contacts)
