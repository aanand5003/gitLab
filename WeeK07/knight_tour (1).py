# shourya raj
from Tour import Tour
from unsorted_list_ADT import*
"""
_author_ = "Shourya Raj"
_IdNumber_ = "28963555"
_email_ = "sraj0008@student.monash.edu"
_date_ = "12/04/2019"
"""


def user():

    next = 0
    action = True
    while action:  # loop to quitting the program
        print("Please print in the format of the two digits like 44 for 4d, 3d for 44, 11 for 1a \n")
        value = input("Enter the value of the function\nstart: 1 \nposition: "              # prompt of choice
                      "2\nundo: 3\nsave: 4\nrestore: 5\nquit: 6\n")

        if value == "1":  # clear                                                           # start
            position = input("Please type the positon of the knight on the chess board:  ")
            assert 11 <= int(position) <= 88 and int(position) % 10 != 0, "Not a valid position"  # condition

            t = Tour(position)                                                               # initializing the class
            next = t.next_moves(position)
            chess_board = t.chess_board()
            print("\nValid Next movements:  ")                                               # Giving direction for the
            print(next[1])                                                                   # first time to the user

            # new_chess = t.show_move()
            # for i in range ((new_chess[0])):
            #    print(new_chess[1][i][1])

        elif(value == "2"):                                                            # position
            stop = False
            while not stop:                                                            # Loop till valid point by user

                print("Please print in the format of the two digits like 44 for 4d, 3d for 44, 11 for 1a \n")
                position = input("Please print the positon of the knight on the chess board:  ")
                assert 11 <= int(position) <= 88 and int(position) and int(position) % 10 != 0, "Not a valid position"

                if next == None :                                                      # No next move
                    print("Please execute start")
                # print(next)

                # checking for the valid move for knight
                bool = t.valid_moves(position, next)                                   # checking next move is valid

                if bool:

                    # print("Valid Position\n")

                    # generating new chess board with positon of the knight

                    next = t.next_moves(position)
                    t.move_knight(position)
                    t.show_move()

                    stop = True
                else:
                    print("Not valid point. Retry please!")

        elif value == "3":            # undo
            try:
                pos = t.undo()
                next = t.next_moves(pos)  # recalculating the moves of knight from the undo position
            except:
                print("Move the knight, can't Undo now")


        elif value == "4":

            t.copy()
        elif value == "5":
            pos = t.restore()
            next = t.next_moves(pos)  # recalculating the position of the knight from the restore copy
            t.show_move()
        elif value == "6":
            action = False



if __name__ == "__main__":
 user()
