"""Olympic"""
def coin(count):
    """จำนวนรางวัล"""
    let = {}
    for _ in range(count):
        land, one, two, three = input().split()
        key = int(one), int(two), int(three)
        lands = let.get(key, [])
        lands.append(land)
        let[key] = sorted(lands)
    total = 1
    for key in sorted(let, reverse=True):
        for jan in let[key]:
            print(total, jan, key[0], key[1], key[2], sum(key))
        total = total + len(let[key])
coin(int(input()))
