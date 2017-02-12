import random

maxTries = 3
a = 1
b = 9
secret = random.randint(a,b)

guess = None
currentTry = 1


while guess != secret and currentTry <= maxTries:
    print "What's the secret number? "
    print "Current try", currentTry

    entry = raw_input()
    guess = int(entry)

    if guess == secret:
        print "Wow, you got it! Congratulation!"

    else:
        currentTry += 1
        print "Sorry, you are wrong. Please try it again!", secret
if guess != secret and maxTries :
    print "Sorry, too many tries."

