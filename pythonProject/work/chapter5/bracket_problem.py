def balance_pairs(brackets: str) -> bool:
    # if brackets.strip() == "" or len(brackets) % 2 == 1:
    if not brackets or len(brackets) % 2 == 1:
        return False

    stack = []
    for bracket in brackets:
        if bracket in "{[(":
            stack.append(bracket)
        elif bracket in "}])":
            peek: str = stack[-1]
            # if peek == "{" or "[" or "(" and bracket == ")" or "]" or "}":
            # if peek == "{" and bracket == "}":
            #     stack.pop()
            # elif peek == "[" and bracket == "]":
            #     stack.pop()
            # elif peek == "(" and bracket == ")":
            #     stack.pop()
            if (peek == "{" and bracket == "}") or (peek == "[" and bracket == "]") or (peek == "(" and bracket == ")"):
                stack.pop()
            else:
                return False
        return True


print(balance_pairs("[]} "))



