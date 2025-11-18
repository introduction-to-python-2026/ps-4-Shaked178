def split_at_digit(s):
    for i, ch in enumerate(s):
        if ch.isdigit():
            return s[:i], int(s[i:])
    return s, 1


def split_before_each_uppercase(formula):
    if not formula:
        return []
    
    result = []
    current_word = ""

    for char in formula:
        if 'A' <= char <= 'Z':
            if current_word:
                result.append(current_word)
            current_word = char
        else:
            current_word += char
            
    if current_word:
        result.append(current_word)
        
    return result
