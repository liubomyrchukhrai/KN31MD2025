class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

    def add(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Inputs must be numbers.")
        return a + b

    def modulus(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a % b
    
    
    def power(self, a, b):
        return a ** b

    def sqrt(self, a):
        if a < 0:
            raise ValueError("Cannot take square root of negative number.")
        return math.sqrt(a)
