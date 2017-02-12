import random
secret = random.randint(1,9)
maxTries = 3

guess = None

for i in range(3):
    print "What's the secret number?"
    print "CurrentTry", i+1

    entry = raw_input()
    guess = int(entry)

    if guess == secret:
        print "Hero!"
        break
    elif i == 2:
        break
    else:
        print "auweh, versuch es noch einmal"


print "Game Over"
