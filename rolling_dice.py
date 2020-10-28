# Rolling two Dice ,ading their values to get the result as exactly 11 to be declared as winner

import random
q=input("ENTER y TO ROLL THE DICE: ")                                      # permission to roll the dice
q=="y"
while q=="y":
    a = ('- - - - -')                                                      # patterns to draw the shape of dice side
    b = ('|       |')
    c = ('| *     |')
    d = ('|   *   |')
    e = ('|     * |')
    f = ('|*     *|')
    def main():
        x = []                                                            # empty list to store the two sides of dice
        for i in range(0, 2):
            m = random.randint(1, 6)
            if m == 1:
                print(a), print(b), print(d), print(b), print(a)          # pattern for 1
            if m == 2:
                print(a), print(c), print(b), print(e), print(a)          # pattern for 2
            if m == 3:
                print(a), print(c), print(d), print(e), print(a)          # pattern for 3
            if m == 4:
                print(a), print(f), print(b), print(f), print(a)          # pattern for 4
            if m == 5:
                print(a), print(f), print(d), print(f), print(a)          # pattern for 5
            if m == 6:
                print(a), print(f), print(f), print(f), print(a)          # pattern for 6
            else:
                pass
            y = m
            x.append(y)                                                   # adding value of sides of dice to list
        print(x)
        z = sum(x)                                                        # sum of values in list
        print(z)
        if z == 11:                                                       # check if sum is equal to 11
            print("Player Won")
        else:
            pass

    main()                                                                # calling the function main
    r = input('ROLL AGAIN?\n ENTER:- yes:y no:n\n ')                      # permission to play again or quit
    if r=="y":
        continue
    else:
        break