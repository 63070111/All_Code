"""[Recommend][Final] War"""
import json
def war(one, two):
    """ค่าศึก"""
    one1 = sorted(json.loads(one), reverse=True)
    two1 = sorted(json.loads(two), reverse=True)
    total = 0
    for i in one1:
        while True:
            if len(two1) > 0:
                jim = two1.pop(0)
                if jim >= i:
                    continue
                elif i > jim:
                    total += i
                    break
            else:
                break
    print(total)
war(input(), input())
