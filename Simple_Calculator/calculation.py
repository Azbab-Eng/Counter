import math
# class calculation:
#     def addition(*param):
#         total = 0
#         for number in param:
#             total += number
#         return total


# add = calculation.addition(2,3,4,5,6)
# print(add)        




def addition(*param):
        total = 0
        for number in param:
            total += number
        return total


def subtraction(x , y):
    return x - y


def division(x , y):
    if x and y != 0:
        return x/y
    else:return "Change your value to integer"
    
        
def multiplication(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total      
        
        
def power(x , y):
        result = math.pow(x , y)
        return result       


def square_root(x):
    return math.sqrt(x)


