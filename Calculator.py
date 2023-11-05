#Your code starts here
class Calculator:
      #Constructor
      def __init__(self):
          pass

      #Method: Function to add the numbers
      def add(self, num1, num2):
        #Exception Handling
          try:
            test = int(num1) + int(num2)
            return test
          except ValueError:
            return "Invalid input"     

      #Method: Function to subtract the numbers
      def subtract(self, num1, num2):
        #Exception Handling
          try:
            test = int(num1) - int(num2)
            return test
          except ValueError:
            return "Invalid input"          

      #Method: Function to multiply the numbers
      def multiply(self, num1, num2):
        #Exception Handling
          try:
            test = int(num1) * int(num2)
            return test
          except ValueError:
            return "Invalid input"          
            
      #Method: Function to divide the numbers
      def divide(self, num1, num2):
        #Exception Handling
          try:
            test = int(num1) / int(num2)        
            return test
          except ValueError:
            return "Invalid input"             
          except ZeroDivisionError:
            return "Divide by 0"