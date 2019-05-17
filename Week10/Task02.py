import numpy as np
"""
Name: Shourya Raj
Email: sraj0008@student.monash.edu
Updated on: 17/05
"""




#def knapsack_value(list_of_items, knapsack_capacity):
 #    table =np.zeros(shape=(len(list_of_items)+1, knapsack_capacity +1))
#
 #    for i, item in enumerate(list_of_items,start=1):
 ##        for j in range(1,knapsack_capacity+1):
 #            if item.weight > j:
#                 table[i, j] =table[i-1, j]
#             else:
 #                table[i,j] = max(table[i-1, j],item.value +table[i-1, j-item.weight])

 #        return table[-1, -1]








def knapSack_dp(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
    array=[]
    value = 0
    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        check =True
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])

            else:
                K[i][w] = K[i - 1][w]
        # stores the result of Knapsack
        res = K[n][W]

        w = W
        for i in range(n, 0, -1):
            if res <= 0:
                break
            if res == K[i - 1][w]:
                continue
            else:

                # This item is included.
                array.append(wt[i - 1])

                # Since this weight is included
                # its value is deducted
                res = res - val[i - 1]
                w = w - wt[i - 1]
    return K[n][W] ,array

def test_knapSack_dp():

   # val = [60, 100, 120]
   # wt = [10, 20, 30]
   # W = 50
    val = [4000, 3500, 1800, 400, 1000, 200]
    wt = [20, 10, 9, 4, 2, 1]

    W = 20
    n = len(val)
    optimal_value, items =(knapSack_dp(W,wt,val,n))
    print("The optimal Value is "+str(optimal_value))
    print("The items associated with optimal Value are " +str(items))


test_knapSack_dp()