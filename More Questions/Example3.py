"""Given a non-negative integer, reverse its digits without converting it to string.
Input:
N = 14503
Output:
out = 30541
"""

def reverse(n):
    rev=0
    while(n>0):
        rem=n%10
        rev=rev*10+rem
        n=n//10
    return rev


n=14503
print(reverse(n))