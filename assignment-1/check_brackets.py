# python3
import sys


class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False


if __name__ == "__main__":
    text = sys.stdin.read()
    result = 'Success'

    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next == '(' or next == '[' or next == '{':
            # Process opening bracket, write your code here
            opening_brackets_stack.append(
                Bracket(next, i + 1)
            )

        if next == ')' or next == ']' or next == '}':
            # Process closing bracket, write your code here
            if not opening_brackets_stack:
                result = i + 1
                break
            else:
                opening_bracket = opening_brackets_stack.pop()
                if opening_bracket.Match(next):
                    pass
                else:
                    result = i + 1
                    break

    if opening_brackets_stack and result == 'Success':
        result = opening_brackets_stack[0].position

    # Printing answer, write your code here
    print(result)
