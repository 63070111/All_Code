"""Password"""
def word(num):
    """รหัส"""
    import hashlib
    total = (hashlib.sha512(str(num).encode("utf-8")).hexdigest()).upper()
    print(total)
word(input())
