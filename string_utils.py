def split_before_each_uppercase(formula):
    if not formula:
        return []

    result = []
    current_word = formula[0]

    for char in formula[1:]:
        if char.isupper():
            result.append(current_word)
            current_word = char
        else:
            current_word += char

    result.append(current_word)
    return result


def split_at_digit(s):
    for i, ch in enumerate(s):
        if ch.isdigit():
            return s[:i], int(s[i:])
    return s, 1


