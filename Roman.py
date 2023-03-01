"""Roman"""
def roman(word):
    """โรมัน"""
    try:
        word = word.upper()
    except AttributeError:
        raise TypeError('expected string, got %s' % type(word))

    numeral_map = (('M', 1000, 3), ('CM', 900, 1), ('D', 500, 1), ('CD', 400, 1),
                   ('C', 100, 3), ('XC', 90, 1), ('L', 50, 1), ('XL', 40, 1),
                   ('X', 10, 3), ('IX', 9, 1), ('V', 5, 1), ('IV', 4, 1), ('I', 1, 3))
    result, index = 0, 0
    for numeral, value, maxcount in numeral_map:
        count = 0
        while word[index: index + len(numeral)] == numeral:
            count += 1
            if count > maxcount:
                raise ValueError('input is not a valid roman numeral: %s' % word)
            result += value
            index += len(numeral)
    if index < len(word):
        raise ValueError('input is not a valid roman numeral: %s' % word)
    return result


print(roman(input()))
