def check_parentheses(string_to_test):
    if not isinstance(string_to_test, unicode):
        raise TypeError
    else:
        count = 0
        for c in string_to_test:
            if c == '(':
                count += 1
            elif c == ')':
                count -= 1
            if count < 0:
                return -1
        if count > 0:
            return 1
        if count == 0:
            return 0
