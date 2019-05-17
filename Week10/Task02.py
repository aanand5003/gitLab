import numpy as np
"""
Name: Shourya Raj
Email: sraj0008@student.monash.edu
Updated on: 15/05
"""




def knapsack_value(list_of_items, knapsack_capacity):
     table =np.zeros(shape=(len(list_of_items)+1, knapsack_capacity +1))

     for i, item in enumerate(list_of_items,start=1):
         for j in range(1,knapsack_capacity+1):
             if item.weight > j:
                 table[i, j] =table[i-1, j]
             else:
                 table[i,j] = max(table[i-1, j],item.value +table[i-1, j-item.weight])

         return table[-1, -1]








def knapSack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]

    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    return K[n][W]

val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print(knapsack_value(val,W))