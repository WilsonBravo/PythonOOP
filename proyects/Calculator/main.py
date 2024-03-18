class calculator:
    def __init__(self, a, b):
        # declarar atributos de la clase
        self.firstNumber=a
        self.secondNumber=b

    # sum method
    def sum(self):
        return (self.firstNumber+self.secondNumber)

    # substract method
    def substract(self):
        return (self.firstNumber-self.secondNumber)
    
    # multiply method
    def multiply(self):
        return (self.firstNumber*self.secondNumber)
    
    # divide method
    def divide(self):
        if self.secondNumber != 0:
            return (self.firstNumber/self.secondNumber)
        else:
            return ("You cannot divide by 0.")
    