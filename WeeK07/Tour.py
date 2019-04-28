from unsorted_list_ADT import *

import copy
"""
_author_ = "Shourya Raj"
_IdNumber_ = "28963555"
_email_ = "sraj0008@student.monash.edu"
_date_ = "12/04/2019"
"""


class Tour:

    def __init__(self, position):
        """
        Constructor function for the Tour class to initilize the values

        :@param position: Take integer or string of number
        @return: No return value
        @post:
        @complexity: best and worst case is  O(1)
        """
        self.position = str(position)
        self.past_position = None
        self.chess = List(0)
        self.size = 8
        self.past_list = List(64)
        self.current_list = List(64)

    def chess_board(self):
        """
         Function to generate the Chess board of 8 * 8 with having number system
         and marked position

        :return: The chess generated chess board
        :@Complexity: best and worst case is O(n^2)
        """
        self.chess = List(self.size)
        for i in range(1, self.size+1):
            dummy_array = List(self.size)

            for j in range(1, self.size+1):
                value = str(i)+str(j)                     # value of number system
                if str(i)+str(j) == self.position:
                    value = "K"

                add_last(dummy_array, value)
            add_last(self.chess, dummy_array)

        return self.chess

    def move_knight(self, pos):
        """
        Function to move the knight position according to the parameter
        and keep the previous position as a record.

        :param pos: Take integer or string of number
        :complexity: best and worst case O(1)
        """

        self.past_position = str(self.position)
        self.position = str(pos)
        add_last(self.past_list, self.past_position)        # Adding for the undo
        add_last(self.current_list, str(pos))               # Adding for the undo function

    def show_move(self):
        """
        Method to show past position and present position of knight on the chess board.

        :return:  The chess board with marked locations of the knight movement.
        :complexity: The best case O(1) and the worst case is O(n)
        """
        past = self.past_position                           # past_location
        current = self.position                             # present location
        location_h = int(past[0])
        location_v = int(past[1])
        print(current)
        self.chess[1][int(current[0])-1][1][int(current[1])-1] = 'k'
        self.chess[1][location_h-1][1][location_v-1] = "*"
        for i in range((length(self.chess))):               # Printing the chess board
            print(self.chess[1][i][1])

        return self.chess

    def next_moves(self, position):
            """
            Method to generate an array of the possible move for the next step of knight
            from the given argument

            :param position: The position should be in the String value of a number.
                              between 11 and 88 excluding multiple of 10
            :return: An List of the possible value of next move.

            :@complexity: best and worst case O(m)
            """
            possible = List(4)                              # Creating an List for looping
            possible_move = List(8)                         # List to keep possible move
            add_last(possible, 1)
            add_last(possible, -1)
            add_last(possible, 2)
            add_last(possible, -2)
            for i in range(length(possible)):               # An algorithm of the next movement of the knight
                value = get_item(possible, i)               # Knight always moves with sum of position [1,-1,2,-2]
                if get_item(possible, i) == 1 or get_item(possible, i) == -1:
                    value = int(position) + (get_item(possible, i)) * 10
                    value1 = value - 2
                    value2 = value + 2

                    if 11 <= value1 <= 88 and value1 % 10 != 0:         # validation of the move
                        add_last(possible_move, value1)
                    if 11 <= value2 <= 88 and value2 % 10 != 0:
                        add_last(possible_move, value2)

                elif get_item(possible, i) == 2 or get_item(possible, i) == -2:
                    value = int(position) + get_item(possible, i) * 10
                    value1 = value - 1
                    value2 = value + 1

                    if 11 <= value1 <= 88 and value1 % 10 != 0:          # validation of the move
                        add_last(possible_move, value1)
                    if 11 <= value2 <= 88 and value2 % 10 != 0:
                        add_last(possible_move, value2)

            return possible_move

    def valid_moves(self, value, moves):
        """
        Method to check the given value is in the array and return in the boolean expression

        :param value: The value is the String an number
        :param moves:  An array generated by the next_moves()
        :return: True or False according to value.
        :complexity: best and worst case O(1)
        """

        bool = False

        if index(moves, int(value)) != None:
          bool = True

        return bool

    def undo(self):
        """

        :return: the Past position of the knight
        :complexity: O(m)
        """
        try:
            past = get_item(self.past_list, length(self.past_list)-1)             # getting previous data of current
                                                                                  # position and previous position
            current = get_item(self.current_list, length(self.past_list)-1)

            delete_item(self.past_list, past)                                     # deleting the data
            delete_item(self.current_list, current)

        except:
            print("Can't Undo after this position....")

        # print("Can't undo without any movement")
        self.position = past
        self.past_position = current

        self.chess[1][int(current[0])-1][1][int(current[1])-1] = current
        self.chess[1][int(past[0])-1][1][int(past[1])-1] = "k"

        for i in range((length(self.chess))):
           print(self.chess[1][i][1])



        return self.position

    def copy(self):
         size = 1
         self.chess_copy = copy.deepcopy(self.chess)
         self.past_list_copy = copy.deepcopy(self.past_list)
         self.current_list_copy = copy.deepcopy(self.current_list)
         self.temp_past  = self.past_position
         self.temp_current= self.position

    def restore(self):

        self.chess = self.chess_copy
        self.past_position = self.temp_past
        self.position = self.temp_current
        self.current_list = self.current_list_copy
        self.past_list = self.past_list_copy
        return self.position


"""t = Tour(88)
chess = t.chess_board()
print(chess)

t.move_knight(67)
new_chess=t.show_move()

t.copy()
t.move_knight(46)
new_chess=t.show_move()


t.move_knight(55)
new_chess=t.show_move()
t.restore()
t.move_knight(58)
t.show_move()
"""