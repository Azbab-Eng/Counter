# SRING VARIABLE METHODS
"""upper() capitalise() lower() title() casefold() count() index()
find() replace() strip() split() just() isupper() islower() istitle()
startswith() endswith() .format() isdigit() isalnum() isalphanum()
rstrip() lstrip() rfind() zfill() rjust() encode() center() join()
isspace() swapcase() splitlines() isprintable() format_map() 
removeprefix() removesufix() """

# String :str = "string variable"
# print(f"Upper case {String.upper()}")
# print(String.capitalize())
# print(String.lower())
# print(String.title())
# print(String.casefold())
# print(String.count("i" , 7,15))
# print(String.index("i" , 7,15))
# print(String.find("n"))
# print(String.replace("i" , "m" , 1))
# String2 :str = "###string###"
# print(String2.strip())
# print(String2.rstrip("#"))
# print(String2.center(20, "*"))

# print(max(2,3,5,6,4,3,5))
# print()
# print(max([2,4,5,7,8,9]))



# try:
#     1/2
# except:
#     print("Error")    
# finally: print ("Program run to the end")


# try:
#     def Seg(x):
#         return x**2
    
    
#     s = Seg(13)
#     print(s)

# except :
#     print("Not square")
# else: print("Else Word")        

# print(Seg(6))
# print(Seg(9))
# print(Seg(3))


# def ZeroDivider():
#     result = 2/2
#     print (f"This is the {result}")


# try:
    # ZeroDivider()
# except:
    # print("It is an Error") 
    # 

# def tryIt(a,b):
#     if b == 0:
#         # raise ZeroDivisionError("Zero Divider")
#         raise ValueError("Cannot divide by Zero")
#     return a/b


# try  :
#     result = tryIt(12,0)
#     print(result)
# except ValueError as e:
#     print(e)    
# except ZeroDivisionError as e:
#     print(e)    


# try :
#     file = open ("compre.py", "r")
#     contents = file.read()
#     print(contents)
# except :
#     print("There is an error in the code")    
# finally: 
#     file.close() 
#     print("The file is closed")


# class raiseError(Exception):
#     def __init__(self,value):
#         self.value = value

#     def __str__(self):
#         return f"Negative value not allowed :{self.value}"

# def check_value(x):
#     if x < 0:
#         raise raiseError(x)        
#     return f"Yes you input above 0"
# try:
#     # check_value(-8)
#     check_value(8)
#     # check_value(-18)
# except raiseError as e:
#     print(e)    


# with open("text.py","a") as file:
#     file.write("print('I am trying if it can work')\n")

# with open("text.py","a") as file:
#     lines = ["""
# def new():
#     print('Let try to do this')
# ""","new()"]
#     file.writelines(lines) 

# with open("text.py","r") as file:
#     contents = file.read()
#     print(contents)


# with open("text.py","r") as file:
#     contents = file.readlines()
#     lst = []
#     for content in contents:
#         lst.append(content )
#         # print(content , end='' )
#     print(lst , end='')


import os 
from pathlib import Path

# abs_path = os.path.abspath('text2.py')
# # print(abs_path)

# if os.path.exists("text.py"):
#     print("The file is exist")

# newFile = Path("text.py")
# # print(newFile)

# if newFile.exists():
#     print("It is exist")

# contents = newFile.read_text()
# print(contents)




























