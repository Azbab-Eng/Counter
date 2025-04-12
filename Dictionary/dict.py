
print("Welcome my User\nI am your Dictionary \nyou can search any words you like about Computer Science")
dictionary = {
    "python" :"Is a high level programming language that is commonly used to AI",
    "ram" :"Read Access Memory is the computer memory that is story current files working on",
    "cpu" :"Centre Proccessing Unit is computer hardware where all the arithementics are process before giving result"

}
while True:
    question = input("What do you want to search or check if not exit/quit >> ").lower()

    if question == "exit" or question.lower() == "quit" :
        print("GoodBye you closed the Dictionary")
        break
    if question in dictionary:
        print(f"{question.capitalize()} : {dictionary[question]}")
    else :
        print(f'Sorry! There is no "{question.capitalize()}" in the Dictionary')
        newWords = input("would you like to add meaning for it no/yes >> ").lower()
        if newWords != "no" and newWords != "":
            meaning = input(f'Enter meaning for the "{question.capitalize()}" >> ')
            if meaning != "":
                dictionary[question] = meaning
                print(f'OK The Dictionary has updated and added "{question.capitalize()}" ')
             

