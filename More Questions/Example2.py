"""Given a string, count the recurrences of alphabets. Count shall not be case-sensitive.
Input:
string = 'I have typed 200 such strings so far!!!'
Output:
out = {'u': 1, 'c': 1, 'n': 1, 'g': 1, 'e': 2, 'h': 2, 'f': 1, 't': 2, 'y': 1, 'r': 2, 's': 4, 'a': 2, 'd': 1, 'v': 1, 'p': 1, 'i': 1, 'o': 1}
Explanation: The input string contains both alphanumeric and special characters, hence we need to ignore numeric and special characters.
Finally, cases are ignored when counting.
"""

def count_occurances(n):
    d1={}
    for i in n:
        if i.isalpha()==True:
            if i not in d1:
                d1.update({i:n.count(i)})
    return d1

string = 'I have typed 200 such strings so far!!!'
print(count_occurances(string))
