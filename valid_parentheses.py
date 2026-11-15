# we are going to use LIFO format and stack
# to solve this problem


"""
THE ALGORITHM :
1.Initialize an empty stack and a map of closing
    brackets to their matching opening brackets:
    ')' -> '(', ']' -> '[', and '}' -> '{'.
2.Iterate through each character c in the string:
        • If c is an opening bracket ('(', '[', or '{'), push it onto the stack.
        • If c is a closing bracket (')', ']', or '}'):
                • Check if the stack is empty. If it is, there is no matching opening bracket, so return false.
                • Pop the top element from the stack and verify that it matches the corresponding opening bracket for c. If it does not match, return false.
3.After checking all characters, return true only
    if the stack is completely empty (meaning all opening brackets were properly closed).

"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in mapping:
                top_ele = stack.pop() if stack else "#"

                if mapping[char] != top_ele:
                    return False
            else:
                stack.append(char)

        return not stack
