class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for bracket in s:
            if bracket == '(' or bracket == '[' or bracket == '{':
                stack.append(bracket)
            elif len(stack) > 0:
                opposite = stack.pop()
                if opposite == '(' and bracket != ')':
                    return False
                if opposite == '{' and bracket != '}':
                    return False
                if opposite == '[' and bracket != ']':
                    return False
            else:
                return False
        return len(stack) == 0