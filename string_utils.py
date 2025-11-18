def split_at_digit(formula):
    for i, ch in enumerate(formula):
        if ch.isdigit():
            return formula[:i], int(formula[i:])
    return formula, 1


def split_before_each_uppercase(formula):
    parts = []
    current = ""
    for ch in formula:
        if ch.isupper() and current:
            parts.append(current)
            current = ch
        else:
            current += ch
    if current:
        parts.append(current)
    return parts

