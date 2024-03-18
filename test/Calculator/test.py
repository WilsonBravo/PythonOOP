def calculatorTest(calculatorClass, a, b):
    calculator=calculatorClass(a, b)
    print("*"*60,f"\nFirst Operand: {a}, Second Operand: {b}\n")
    print(f"SUMA:{calculator.sum()}")
    print(f"RESTA:{calculator.substract()}")