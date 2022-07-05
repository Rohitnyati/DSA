"""For a given array with repeated elements, exactly one element is not repeated (single).
Find the non-repeated element. Try to find a solution with linear time complexity.
Input:
N = [1, 2, 5, 4, 6, 8, 9, 2, 1, 4, 5, 8, 9]
Output:
out = 6
Explanation: In the given array, all elements are repeated except 6.
"""
def not_repeated(n):
    for i in n:
        if n.count(i)==1:
            return i

N = [1, 2, 5, 4, 6, 8, 9, 2, 1, 4, 5, 8, 9]
print(not_repeated(N))
