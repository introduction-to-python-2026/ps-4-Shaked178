def split_before_each_uppercase(formula):
    if not formula:
        return []
    result = []
    current = formula[0]
    for char in formula[1:]:
        if char.isupper():
            result.append(current)
            current = char
        else:
            current += char
    result.append(current)
    return result

def split_at_digit(s):
    for i, ch in enumerate(s):
        if ch.isdigit():
            return (s[:i], int(s[i:]))
    return (s, 1)



