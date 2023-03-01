"""[Midterm] RightArrow"""
def arrow(first, seconds):
    """RightArrow"""
    for i in range(0, seconds//2):
        print(i * " " + "*" * first)
    print(seconds//2*" " + "*"*first)
    for j in range(seconds//2-1, -1, -1):
        print(j * " " + "*" * first)

arrow(int(input()), int(input()))
