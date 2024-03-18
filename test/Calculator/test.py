def calculatorTest(calculatorClass, a, b):
    calculator=calculatorClass(a, b)
    print("*"*60,f"\nFirst Operand: {a}, Second Operand: {b}\n")
    print(f"ADDITION: {calculator.sum()}")
    print(f"SUBSTRACTION: {calculator.substract()}")
    print(f"MULTIPLICATION: {calculator.multiply()}")
    print(f"DIVISION: {calculator.divide()}")