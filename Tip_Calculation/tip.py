# import re , sys

# def Bill_calculation():
#     time_used = input("How many months your bill covered? (02 months) >> ")
#     tip = input("What do you want give us as competiation? (400) naira >> ")
#     # time = re.match(r'^\d{1,2} :[0-5]\d$', time_used)
#     time = time_used[0:2]
    
#     if time.isdigit() and tip.isdigit():
#         time = int(time)
#         tip = int(tip)
#     else : 
#         print("Please follow the format gave to you (02 months) (400) naira")
#         quit() 

#     level = input("Please chooce your Plan premium(#950) / normal(#500) >>")
#     if level.lower() == "premium":
#         days = time * 30
#         result = (days * 950) + tip
        
#     elif level.lower() == "normal" :
#         days = time * 30
#         result = (days * 500) + tip
#     else :
#         print("Make sure you make a choice")
#         quit()

#     print(f"Your total bill is #{result} in {time}months.")
 

# Bill_calculation()


# re.match(r'^\d{1,2}:[0-5]\d$',wake)


def Bill_calculation2():
    time_used = input("How many months your bill covered? (02 months) >> ")
    tip = input("What do you want give us as competiation? (400) naira >> ")
    # time = re.match(r'^\d{1,2} :[0-5]\d$', time_used)
    # time = time_used[0:2]
    if time_used.endswith("days"):
        time = time_used.replace("days" , "")
        time = time.strip()
        if time.isdigit() and tip.isdigit():
            time = int(time)
            tip = int(tip)
        else : 
            print("Please follow the format gave to you (02 months) (400) naira")
            quit() 
        level = input("Please chooce your Plan premium(#950) / normal(#500) >>")
        if level.lower() == "premium":
            days = time 
            result = (days * 950) + tip
            
        elif level.lower() == "normal" :
            days = time
            result = (days * 500) + tip
        else :
            print("Make sure you make a choice")
            quit()    
    elif time_used.endswith("months"):
        time = time_used.replace("months" , "")
        time.strip()
        if time.isdigit() and tip.isdigit():
            time = int(time)
            tip = int(tip)
        else : 
            print("Please follow the format gave to you (02 months) (400) naira")
            quit()
        level = input("Please chooce your Plan premium(#950) / normal(#500) >>")
        if level.lower() == "premium":
            days = time * 30
            result = (days * 950) + tip
            
        elif level.lower() == "normal" :
            days = time * 30
            result = (days * 500) + tip
        else :
            print("Make sure you make a choice")
            quit()     
    else: print("Input correct value")    
   

    print(f"Your total bill is #{result} in {time} days/months.")
 

Bill_calculation2()