# Here's an example of insecure code in Python that uses the eval() function to execute arbitrary user input

def calculate(expression):
    result = eval(expression)
    print("The result is:", result)
