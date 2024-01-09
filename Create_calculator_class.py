"""
Create a class that has basic calculating functions.

You can have as many methods as you like but here are few suggestions.
* method to take two numbers and add them and return the sum
* method to take two numbers and subtract the second number from the first number and return the diff
* method to take two numbers and return the multiplication of the two
* method to divide two numbers and return the result (first number divided by second number)

"""

class  BasicCalculator:
    @staticmethod
    def add(x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y  # Fixed the missing operand '*'

    def divide(self, x, y):
        return x / y

# Creating an instance of BasicCalculator
mycalc = BasicCalculator()

# Using the methods
my_sum = mycalc.add(4, 6)
print(my_sum)

class BasicCalculatorV2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def subtract(self):
        return self.x - self.y

    def multiply(self):
        return self.x * self.y

    def divide(self):
        return self.x / self.y

# Creating an instance of BasicCalculatorV2 with initial values
mycalc2 = BasicCalculatorV2(17, 20)

# Using the methods
my_sum = mycalc2.add()
print(my_sum)
