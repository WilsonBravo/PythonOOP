def calculatorTest(calculatorClass, a, b):
    calculator=calculatorClass()
    print("*"*60,f"\nFirst Operand: {a}, Second Operand: {b}\n")
    print(f"ADDITION: {calculator.sum(a, b)}")
    print(f"SUBSTRACTION: {calculator.substract(a, b)}")
    print(f"MULTIPLICATION: {calculator.multiply(a, b)}")
    print(f"DIVISION: {calculator.divide(a, b)}")