"""[Midterm] Sequence XXX"""
def box(one, two):
    """สร้างกล่อง"""
    for numx in range(one):
        for _ in range(two):
            for numy in range(one):
                if numx == 0 or numy == 0 or numx == one-1 or numy == one-1\
                        or numx == one-numy-1 or numx == numy:
                    print("*", end="")
                else:
                    print(" ", end="")
            print(" ", end="")
        print()
box(int(input()), int(input()))
