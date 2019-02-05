from SenseHatHangman import SenseHatHangman

def game():
    screen = SenseHatHangman()
    screen.start()
    secret = input("Enter word:")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    answer = [] #simple way of creating empty strings, could be answer = list()
    for i in range(len(secret)):
        answer.append("_")
    equal = False
    wrong = 0
    while wrong < 10 and equal != True:
        guess = input("Enter letter:")
        listLet = secret.split()
        find = False 
        for x in range(0, len(secret)):
            if secret[x] == guess:
                answer[x] = guess
                find = True
        equal = ''.join(answer) == ''.join(listLet)
        #equal = (answer > listLet) - (answer < listLet)  == 0 # just checking if w and listLet are equal

        if find == True:
            print("Good, the string is now: ", ''.join(answer))
        else:
            print("Wrong!")
            screen.wrongGuess()
            wrong += 1
    if equal == True:
        print("You won!")
        screen.winner(secret)
    else:
        print("You lose!")
        

def main():
    game()

if __name__ == '__main__':
    main()
