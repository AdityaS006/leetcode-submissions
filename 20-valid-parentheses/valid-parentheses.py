class Solution:
    def isValid(self, s: str) -> bool:
        b={')':'(',']':'[','}':'{'}
        n=len(s)
        if n%2 !=0:
            return False
        stack=[]
        for char in s:
            if char in b:
                top_element = stack.pop() if stack else '#'
                
                if b[char] != top_element:
                    return False
            else:
                # It's an opening bracket, push it onto the stack
                stack.append(char)
               
        return not stack