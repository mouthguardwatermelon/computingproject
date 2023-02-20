import random

WORDS = ["python", "jumble", "easy", "difficult", "answer",  "xylophone"]
word = random.choice(WORDS)
word_list = list(word)
attempts = 15
results_list = (" " * len(word))
results_list = list(results_list)
reference = (" "*len(word))
reference_list = list(reference)
while True:
    letter = input("Please type in a letter:")
    if letter in word_list:
        num1 = word_list.index(letter)
        results_list[num1] = letter
        word_list[num1] = " "
        attempts -= 1
        print("Correct!")
        print(f"{results_list}(Attempts left:{attempts})")
        
    elif letter not in word_list:
        print("Wrong!")
        attempts -= 1
        print(f"{results_list}(Attempts left:{attempts})")
  
    if word_list == reference_list:
        print("Congratulations! You solved it!!")
        break
    if attempts == 0:
        print("Aw :( Next time maybe :<")
        break
    
