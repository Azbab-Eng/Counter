import re , sys
print("Welcome to Bot_Game ")
start_game = input("Do you like to chat with me? (yes)/(no)  >>")
if start_game.lower() != "yes":
    print("GoodBye you are not ready to chat.")
    quit()

def Bot_game():    
    name = input("What is your name :) ")
    greeting = 'Welcome' , name , 'Your Name is Amaizing'
    print(greeting)
    start = input("Are you ready to go with me :) ")
    grant = 0
    if start.lower() != "yes":
        print("Let me know when you ready to chat with me.")
        quit()

    wake = input("When do you wake up in the morning? (5:00am) ")
    if re.match(r'^\d{1,2}:[0-5]\d$',wake):
        hour , minute = wake.split(":")
        hour = int(hour)
        # print(hour, "and" , minute)
        if hour >= 6 :
            print("""Seem like you didn't wake up to Tahaajud
        and not pray Fajir Naflah,
        Try to be waking up before 5am to ensure all these Nawaafil""")
        else:
            print("Wow it looks like you wake up for Taahaajud (Baarokallah Fiih)")
            grant += 1        
            
    else: 
        print("It is not a Nemeric, write with this format (5:00)")
        sys.exit()    
    food = input("What do you like to eat Semo/Bread/Grain or Nothing :) ").lower()
    if food == "bread":
        grant += 1
        print("Yes bread is kind of good food you can eat in the morning, Try to eat it with good Protein")
    elif food == "semo":
        print("Semo will too heavy in your stomach, You can try eat Bread or any soft food")
    elif food == "grain":
        print("It is not good for you to eat Grain in the morning except you take good Protein ")
    else:    
        print("It is dangerous for you to not eat, You are getting out to work")        
    print(f"You grant {grant} times")


Bot_game()