class calculator:
    # sum method
    def sum(self, firstNumber, secondNumber):
        return (firstNumber+secondNumber)

    # substract method
    def substract(self, firstNumber, secondNumber):
        return (firstNumber-secondNumber)
    
    # multiply method
    def multiply(self, firstNumber, secondNumber):
        return (firstNumber*secondNumber)
    
    # divide method
    def divide(self, firstNumber, secondNumber):
        if secondNumber != 0:
            return (firstNumber/secondNumber)
        else:
            return ("You cannot divide by 0.")
    