
"""Write a Python class to find validity of a string of parentheses, '(', ')', '{', '}', '[' and '].
These brackets must be close in the correct order, for example "()" and "()[]{}" are valid but
"[)", "({[)]" and "{{{" are invalid.
Input: parenthese_str = "(){}[]"
Output: out = True
Input: parenthese_str = "({}[])"
Output: out = True
Input: parenthese_str = "({)}"
Output: out = False
"""

def check_paranthesis(paranthesis_str):
    stack=[]
    for paranthesis in paranthesis_str:
        if paranthesis in ["(","{","["]:
            stack.append(paranthesis)
        else:
            if not stack:
                return False
            current_paranthesis=stack.pop()
            if current_paranthesis=='(':
                if paranthesis !=")":
                    return False
            if current_paranthesis=='{':
                if paranthesis != "}":
                    return False
            if current_paranthesis=='[':
                if paranthesis !="]":
                    return False

    if stack==[]:
        return True
    return False


check_paranthesis("(){}[")