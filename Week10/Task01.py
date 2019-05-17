"""
Name: Shourya Raj
Email: sraj0008@student.monash.edu
Updated on: 15/05
"""

def fibbonacci(n):
    """

    :param n: An integer value should be greater and equals to the 0
    :return: returns the sum of the last two numbers
    """
    if n == 0 or n == 1:
        return n
    return fibbonacci(n-1)+fibbonacci(n-2)


def fib(n):
  return fib_aux(n,0,1)

def fib_aux(n, before_last, last, i=0):
    """

    :param n:
    :param before_last:
    :param last:
    :param i:
    :return:
    """
    if n ==0:
        return before_last, i
    else:
        i +=1
        return fib_aux(n-1, last, before_last+last, i)


def fib_dp(n):
    mem = [None] * (n + 1)
    mem[0] = 0
    mem[1] = 1

    for i in range(2, n + 1):
        mem[i] = mem[i - 1] + mem[i - 2]
    return mem[n]
