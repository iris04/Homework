import random

secret = {random.randint(1, 20)}
i = 0
while i < 5:
    guess = int(raw_input("Guess what number it is: "))

    if guess == secret:
        print "Wow, you got it! Congratulation!"
        break
    else:
        print "Sorry, you are wrong. Please try it again!"
        print secret

