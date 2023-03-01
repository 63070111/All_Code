"""ChristmasTree"""
def christmas(tree, bole):
    """สร้างรูปต้นไม้"""
    for i in range(1, 2*tree, 2):
        print(("*"*i).center(tree*2))
    for i in range(bole):
        print(("---").center(tree*2))
christmas(int(input()), int(input()))
