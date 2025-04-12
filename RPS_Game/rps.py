import random 

# setting variable for computer, player and options
# ask for the time playing
# check if the time playing is digit
#  set loop for time playing 
# set random variable for computer 
# ask player to choose the option
# check if the optin choose is the same with computer random 
# update score for computer and player

computer_score = 0
player_score = 0
option = ["rock","paper","scisors"]
time_playing = input("How many times you want to play >> ")
time_playing = time_playing.strip()
if time_playing.isdigit():
    time_playing = int(time_playing)
    # print(time_playing)
    start = 1
    while start <= time_playing :
        player_choose = input("Make your choice Rock/Paper/Scisors >> ").lower()
        player_choose = player_choose.strip()
        computer_choose = random.choice(option)
        if player_choose in option :
            if player_choose == computer_choose:
                player_score += 1
            else: 
                computer_score += 1    
        else :
            print("Input correct word")
        #print(f" You choose {player_choose} and computer choose {computer_choose}")
        start += 1
        continue
    print(f"You win {player_score} times and computer win {computer_score} ")
else: 
    print("Make sure you input time you want to play in Digit.") 
    quit()

