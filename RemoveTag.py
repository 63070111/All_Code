"""RemoveTag"""
def tag(word):
    """เอา tag ออก"""
    while '<' in word:
        word = word[:word.find('<')] + ' ' + word[word.find('>') + 1:]
    print(word.split())
tag((input()))
