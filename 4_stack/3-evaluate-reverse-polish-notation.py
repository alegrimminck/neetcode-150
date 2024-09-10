from types import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            match t:
                case "+":
                    stack.append(stack.pop() + stack.pop())
                case "*":
                    stack.append(stack.pop() * stack.pop())
                case "/":
                    a, b = stack.pop(), stack.pop()
                    stack.append(int(b / a))
                case "-":
                    a, b = stack.pop(), stack.pop()
                    stack.append(b - a)
                case _:
                    stack.append(int(t))
        return stack[0]
