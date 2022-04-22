# Define a class which has at least two methods:

# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

# Hints:
# Use init method to construct some parameters

class MyString:

  def __init__(self):
    self.input = ""

  def getString(self):
    self.input = input("enter an input ")

  def printString(self):
    return self.input.upper()

stringObject = MyString()
stringObject.getString()
print(stringObject.printString())

  
  