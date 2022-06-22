import time
#pauses
import os
#to clear screen
import random
#for the computer 


def tic_tac_toe(ForS):
    #start of game

    os.system('clear')
    if ForS == "f":
        print("You are first!")

    if ForS == "s":
        print("You are second! Type 'skip' on your first turn!")

    time.sleep(2)
    #clears screen 

    print("")
    print(""" 
  1 | 2 | 3
  _________
  4 | 5 | 6
  _________
  7 | 8 | 9
  """)
  #show board

    print("")
    print("Each number corresponds with a square on the tic tac toe board.")
	#explain
    print("")

    print("You are 'O'. \n")
	#explain
    time.sleep(2)
    os.system('clear')
    print("")
    t1 = " |"
    t2 = "   "
    t3 = "|"
    t4 = "_______"
    t5 = " |"
    t6 = "   "
    t7 = "|"
    t11 = "_______"
    t8 = " |"
    t9 = "   "
    t10 = "|"
    print(t1 + t2 + t3 + "\n" + t4 + "\n" + t5 + t6 + t7 + "\n" + t11 + "\n" +
          t8 + t9 + t10 + "\n")
	#this createed the board, entering for new lines

    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "skip"]
	#skip is being used to prevent code from breaking

    x = None  #x = Player Numbers
    y = None  #y = Opponent Random
    h1 = 0
    h2 = 0
    h3 = 0
    h5 = 0
    h6 = 0
    h7 = 0
    h8 = 0
    h9 = 0
    h10 = 0
    blocky = 0
    done = 0
    won = 2
    done = 2

	#variables

    for i in range(20):
        #start loop, 20 is random number

        print("<<<<>>>> \n")
        print("""1 | 2 | 3
_________
4 | 5 | 6
_________
7 | 8 | 9""", "(each section corresponds to a square.)")

        print("\n <<<<>>>> \n")
        print(numbers, ": are the numbers you can choose from.")
        print("<<<<>>>> \n")
        x = input("Which do you choose: ")
		#pick a number

        while x not in numbers:
            print(numbers, ": are the numbers you can choose from.")
            print("<<<<>>>> \n")
            x = input("Which one do you choose: ")
            if len(numbers)==0:
                break
			#if number is already in use

        numbers.remove(x)
		#remove number after use

   
        y = str(random.choice(numbers))
        print("The computer chose: ", y)
        time.sleep(3)
        numbers.remove(y)
		#this is computer number choice, and computer number remove


        #h1 h2 hf3
        #h5 h6 h7
        #h8 h9 h10
        #1 2 3
        #4 5 6
        #7 8 9
		#grid 1 (actual positive (player) and negative (computer))

		#t1 t2 t3
   		#t5 t6 t7
    	#t8 t9 t10
    	#1 2 3
    	#4 5 6
    	#7 8 9
		#grid 2 (this is for X and O displayed on screen)




        print("")
        print(y, blocky)
        if x == "1" or y == "1":
            if x == "1":
                t1 = "O|"
                h1 = "positive"
                t4 = "_______"
            elif y == "1":
                t1 = "X|"
                h1 = "negative"
                t4 = "_______"

        if x == "2" or y == "2":
            if x == "2":
                t2 = " O "
                h2 = "positive"
                t4 = "_______"
            elif y == "2":
                t2 = " X "
                h2 = "negative"
                t4 = "_______"


        if x == "3" or y == "3":
            if x == "3":
                t3 = "|O"
                h3 = "positive"
                t4 = "_______"
            elif y == "3":
                t3 = "|X"
                h3 = "negative"
                t4 = "_______"

        if x == "4" or y == "4":
            if x == "4":
                t5 = "O|"
                h5 = "positive"
                t11 = "_______"
                t4 = "_______"
            elif y == "4":
                t5 = "X|"
                h5 = "negative"
                t11 = "_______"
                t4 = "_______"

        if x == "5" or y == "5":
            if x == "5":
                t6 = " O "
                h6 = "positive"
                t11 = "_______"
                t4 = "_______"
            elif y == "5":
                t6 = " X "
                h6 = "negative"
                t11 = "_______"
                t4 = "_______"

        if x == "6" or y == "6":
            if x == "6":
                t7 = "|O"
                h7 = "positive"
                t11 = "_______"
                t4 = "_______"
            elif y == "6":
                t7 = "|X"
                h7 = "negative"
                t11 = "_______"
                t4 = "_______"

        if x == "7" or y == "7":
            if x == "7":
                t8 = "O|"
                h8 = "positive"
                t11 = "_______"
                t4 = "_______"
            elif y == "7":
                t8 = "X|"
                h8 = "negative"
                t11 = "_______"
                t4 = "_______"

        if x == "8" or y == "8":
            if x == "8":
                t9 = " O "
                h9 = "positive"
                t11 = "_______"
            elif y == "8":
                t9 = " X "
                h9 = "negative"
                t11 = "_______"

        if x == "9" or y == "9":
            if x == "9":
                t10 = "|O"
                h10 = "positive"
                t11 = "_______"
            elif y == "9":
                t10 = "|X"
                h10 = "negative"
                t11 = "_______"

        os.system('clear')
        print(t1 + t2 + t3 + "\n" + t4 + "\n" + t5 + t6 + t7 + "\n" + t11 +
              "\n" + t8 + t9 + t10 + "\n")

		#row top horizontal
        if h1 == h2:
            if h2 == h3:
                if h3 == h1:
                    if h3 == "positive":
                        print("You won!")
                        won = 1
                        break
                    elif h3 == "negative":
                        print("You lost!")
                        won = 0
                        break

        #row middle horizontal
        if h5 == h6:
            if h6 == h7:
                if h7 == h5:
                    if h5 == "positive":
                        print("You won!")
                        won = 1
                        break
                    elif h5 == "negative":
                        print("You lost!")
                        won = 0
                        break
 
        #row bottom horizontal
        if h8 == h9:
            if h9 == h10:
                if h8 == h10:
                    if h8 == "positive":
                        print("You won!")
                        won = 1
                        break
                    elif h9 == "negative":
                        print("You lost!")
                        won = 0
                        break

        #diagonal top left to bottom right
        if h1 == h6:
            if h6 == h10:
                if h10 == h1:
                    if h6 == "positive":
                        print("You won!")
                        won = 1
                        break
                    elif h6 == "negative":
                        print("You lost!")
                        won = 0
                        break

        #diagonal top right to bottom left
        if h3 == h6:
            if h6 == h8:
                if h3 == h8:
                    if h8 == "positive":
                        print("You won!")
                        won = 1
                        break
                    elif h8 == "negative":
                        print("You lost!")
                        won = 0
                        break

        #vertical left row
        if h5 == h1:
            if h5 == h8:
                if h1 == h8:
                    if h5 == "positive":
                        print("You won!")
                        won = 1
                        break
                    elif h5 == "negative":
                        print("You lost!")
                        won = 0
                        break

        #vertical middle
        if h2 == h6:
            if h9 == h6:
                if h2 == h9:
                    if h2 == "positive":
                        print("You won!")
                        won = 1
                        break
                    elif h2 == "negative":
                        print("You lost!")
                        won = 0
                        break

        #vertical right
        if h3 == h7:
            if h10 == h7:
                if h10 == h3:
                    if h3 == "positive":
                        print("You won!")
                        won = 1
                        break
                    elif h3 == "negative":
                        print("You lost!")
                        won = 0
                        break

        if done == 1:
            break
        print("Next turn. \n")
  
    time.sleep(2)
    time.sleep(1)
    os.system('clear')
    time.sleep(1)
    if won == 1:
        print("You won, and beat the opponent!")
        print("Good job!")
    elif won == 0:
        print("You lost.")
        print("Good try!")
    elif done == 1:
        print("It's a tie.")
        print("Good job.")
    #win conditions

#end of game

symbol = input("Do you want to go first or second (f/s): ")
tic_tac_toe(symbol)
again = input("Want to go again?(y/n): ")
if again == "y":
	os.system('clear')
	tic_tac_toe()
if again == "n":
	print("Thanks for playing!")
#call function for game!
#TIC TAC TOE!!!!!!!!!!!!
