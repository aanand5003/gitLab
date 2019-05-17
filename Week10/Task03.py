
"""
@name: Shourya Raj
@email id: sraj0008@student.monash.edu
@updated on: 17/05
"""
import timeit
# Naive

def knapSack_na(W, wt, val, n):
    # Base Case
    if n == 0 or W == 0:
        return 0

    # If weight of the nth item is more than Knapsack of capacity
    # W, then this item cannot be included in the optimal solution
    if (wt[n - 1] > W):
        return knapSack_na(W, wt, val, n - 1)

        # return the maximum of two cases:
    # (1) nth item included
    # (2) not included
    else:
        return max(val[n - 1] + knapSack_na(W - wt[n - 1], wt, val, n - 1),
                   knapSack_na(W, wt, val, n - 1))



# Dynammic programming


# A Dynamic Programming based Python Program for 0-1 Knapsack problem
# Returns the maximum value that can be put in a knapsack of capacity W
def knapSack_dp(W, wt, val, n):
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

val = [4000, 3500, 1800, 400, 1000, 200]
wt = [20, 10, 9, 4, 2, 1]

W = 20
#val = [60, 100, 120]
#wt = [10, 20, 30]
#W = 50
n = len(val)
start_na = timeit.default_timer()
print("Value using the Naive approach " +str(knapSack_na(W, wt, val, n)))
stop_knapSack_na = timeit.default_timer() - start_na
print(stop_knapSack_na)
start_dp = timeit.default_timer()
print(knapSack_dp(W,wt,val,n))
stop_knapSack_dp = timeit.default_timer() - start_dp


print(stop_knapSack_dp)


# conclusion:
# If N is larger and weight is less then use dp otherwise use resurssivee approach
# Because of W*N and 2^N
