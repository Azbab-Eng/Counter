import random
user_score = 0
computer_score = 0
no_range = input("Enter the range of guess number :)")

if no_range.isdigit():
    while True:
        no_range = int(no_range)
        computer_guess = random.randint(0,no_range)
        user_guess = input(f"Guess any number from 0-{no_range} >>")
        if user_guess.isdigit():
            user_guess = int(user_guess)
            if computer_guess == user_guess:
                user_score += 1
                print("Yes you got it")
                break
            elif computer_guess < user_guess:
                computer_score += 1
                print("You make above the answer")
            else:
                computer_score += 1
                print("You make below the answer")    
        else: 
            print(f"Input integer number from 0-{no_range}")
            continue
else:
    print("input integer number Next time")
    quit()
      
print(f"You score {user_score} , computer score {computer_score}")      