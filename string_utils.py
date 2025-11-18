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


def split_at_digit(formula):
    for i, ch in enumerate(formula):
        if ch.isdigit():
            return formula[:i], int(formula[i:])
    return formula, 1


