
def sum(first, second):
    return first + second
    
def subtract(first, second):
    return first - second
    
def multiply(first, second):
    return first * second
    
def divide(first, second): 
    return first / second
    
def exponent(first, second):
    return first**second

def square(int): 
     return int ** 2
 
def sqrt(int):
    return int**(1/2.0)
 
def cube(int):
    return int** 3

from math import sin

def sin(float):
     return float

from math import cos

def cos(float): 
    return float

from math import log

def log(float):
    return float

print 'Welcome to the scientific calculator using python!'

print "To add numbers, please enter 'add'."
print "To subtract numbers, please enter 'minus'."
print "To multiply numbers, please enter 'multi'."
print "To divide numbers, please enter 'div'."
print "To exponent numbers, please enter 'exp'."
print "To square number, please enter 'sq'."
print "To squareroot a number, please enter 'sqrt'."
print "To cube a number, please enter 'cube'."
print "To find the sin of an angle, please enter 'sin'."
print "To find the cos of an angle, please enter 'cos'."
print "To find the log of an angle, please enter 'log'."

def calculator():
    
    user_choice = raw_input("Enter choice:")
    
    num1 = int(raw_input("Enter first number: "))
    num2 = int(raw_input("Enter second number: "))

    if user_choice == 'add':
        print sum(num1,num2)

    elif user_choice == 'subtract':
        print subtract(num1,num2)

    elif user_choice == 'multi':
        print multiply(num1,num2)

    elif user_choice == 'div':
        print divide(num1,num2)
   
    elif user_choice == 'exp':
        print exponent(num1, num2)
    
    elif user_choice == 'sq':
        print square(num1)
    
    elif user_choice == 'sqrt':
        print sqrt(num1)
    
    elif user_choice == 'cube':
        print cube(num1)
    
    elif user_choice == 'sin':
        print sin(num1)

    elif user_choice == 'cos':
        print cos(num1)
    
    elif user_choice == 'log':
        print log(num1)
        
    else:
        print("Invalid input")
        
    s_choice = raw_input("Press 'Y' to do another calculation or press 'N' to quit:")
    
    s_choice.lower()
    
    if s_choice == 'N':
        quit
    elif s_choice == 'Y':
        calculator()
        
if __name__ == '__main__':
    calculator()