class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {')':'(', '}':'{',']':'['}
        for i in s:
            if i in brackets:
                if stack:
                    last = stack.pop()
                    if brackets[i]!=last:
                        return False
                else:
                    return False
            else:
                stack.append(i)
        return len(stack)==0