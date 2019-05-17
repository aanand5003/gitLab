"""
Name: Shourya Raj
Email: sraj0008@student.monash.edu
Updated on: 17/05
"""


def cost(M, start, end, word):
    """
    @precondition: The value of the word should be an string
    :param M: An positive Integer of the size of the charachter
    :param start: The starting value
    :param end: The ending value
    :param word: The word going to be executed
    :return: Returning the cost
    @postcondition: return "inf" when value is less than 0
    """
    i = start
    sum_value = 0
    while i <= end:
        sum_value += len(word[i])
        i += 1

    sum_value += end-start                    # calculate the sum
    if sum_value < 0:
        return float('inf')                   # show inf if sum is negative

    cost_value = (M-sum_value)**3             # calculating final cost
    if cost_value < 0:
        return float('inf')                   # show inf if cost is negative

    return cost_value


if __name__ == '__main__':

    text = "you can use dynamic programming to justify text and I learned that in FIT1008"
    word = text.split(" ")                                  # split the text
    n = len(word)
    M = 15
    table = [None]*n                                        # create array of length n
    for i in range(n):
        table[i] = [None]*n                                 # create another array inside the array

    for i in range(n):
        for j in range(n):
            table[i][j] = cost(M, i, j, word)               # put the cost into the table

    for i in range(n):
        print(table[i])                                     # printing table

