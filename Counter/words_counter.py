
def Counter():
    print("Welcome to Words or Letters Counter \n I can help you count your words or letters")
    sentence = input("Write or paste sentence .")
    
    
    a = 1
    while a <= 5:
        letter_or_word = input("Input the word or letter you want to counter.")
        result = sentence.count(letter_or_word)
        if result == 0:
            print(f"We could not see '{letter_or_word}' in the sentence try another letter")
        else:print(f'we can see "{letter_or_word}" in {result} times in that sentence ')
        a += 1
        continue


Counter()
