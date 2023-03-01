"""Robot I"""
def robot(name, age):
    """robot"""
    if age < 18:
        print(name+",", "you can pass.")
    else:
        print(name+",", "you shall not pass.")
robot(input(), float(input()))
