"""FibonacciRecursionV2"""
def order(word, value):
    """เปลี่ยน"""
    if word in value:
        return value[word]
    if word > 500:
        order(word-500, value)
    total = order(word-2, value) + order(word-1, value)
    value[word] = total
    return total
print(order(int(input()), {0:0, 1:1}))
