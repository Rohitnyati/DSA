"""Given a dictionary consisting of non-negative integer keys and values,
find the values corresponding to even keys and subtract 1 from each of those values.
Return a list containing all the modified values.
Input:
dict1 = {1: 111, 2: 22, 3: 5, 8: 10, 12: 13, 0:11}
Output:
out = [21, 9, 12]
Explanation: Even keys in the dictionary are 2, 8, 12. Values corresponding to these keys are 22, 10, 13.
Output list contains values subtracted by 1. Note that 0 is not an even number.
"""

def find_even_keys(n):
    for i in n.keys():
        if i%2==0 and i!=0:
            print(n[i]-1)

dict1 = {1: 111, 2: 22, 3: 5, 8: 10, 12: 13, 0:11}
d1=find_even_keys(dict1)