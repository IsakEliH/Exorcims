def is_paired(input_string):
    BRACKETS: dict[str, str] = {")": "(", "}": "{", "]": "["}
    OPENERS: set = set(BRACKETS.values())
    CLOSERS: set = set(BRACKETS)

    stack: list = []

    for char in input_string:
        if char in OPENERS:
            stack.append(char)
        elif char in CLOSERS:
            if len(stack) == 0:
                return False

            top = stack.pop()
            if top != BRACKETS[char]:
                return False

    return len(stack) == 0
