'''
LeetCode #20: Valid Parentheses  
Date: Feb 02, 2026  
Difficulty: Easy  
Pattern: Stack  
Time Complexity: O(n)  
Space Complexity: O(n)  

Problem:  
Given a string containing '()', '{}', and '[]',  
determine if the string is valid.  

A string is valid if:  
- Every opening bracket has a matching closing bracket.  
- Brackets are closed in the correct order.  

Approach:  
Use a stack to track opening brackets.  
Create a mapping of closing to opening brackets.  
For each character in the string:  
- If it is an opening bracket, push it onto the stack.  
- If it is a closing bracket, check the top of the stack:  
  - If it matches, pop the stack.  
  - Otherwise, return false.  
At the end, if the stack is empty, return true.  
'''
• explanation
• code

class Solution:
    def isValid(self, s):
        stack = []  # stack to store opening brackets
        pairs = {')': '(', '}': '{', ']': '['}  # mapping closing → opening

        for char in s:
            if char in pairs.values():  # if opening bracket
                stack.append(char)
            elif char in pairs:  # if closing bracket
                if stack and stack[-1] == pairs[char]:  # top matches?
                    stack.pop()
                else:
                    return False  # mismatch or empty stack
            else:
                return False  # invalid character (optional)

        return not stack  # stack empty → valid
