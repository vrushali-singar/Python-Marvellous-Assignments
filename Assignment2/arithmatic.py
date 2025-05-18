#module for assigment2_1.py Q 
def add(value1,value2):
    result = value1 + value2
    return result
def sub(value1,value2):
    result = value1 - value2
    return result
def mult(value1,value2):
    result = value1 * value2
    return result
def div(value1,value2):
    if value2 != 0:  
        result = value1 / value2
        return result
    else:
        return "Cannot divide by zero"
