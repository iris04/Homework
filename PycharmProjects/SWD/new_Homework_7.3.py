import random

def main():

    tries = 0
    secret = random.randint(1, 20)



    while tries < 3:
        guess = raw_input("Guess what number it is: ")
        guess = int(guess)
        tries += 1

        if guess == secret:
            print "Wow, you got it! Congratulation!"
            break
        else:
            print "Sorry, you are wrong. Please try it again! It is %s" %secret

if __name__ == '__main__':
    main()