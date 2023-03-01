"""[Final] Inverter"""
def number(value):
    """สลับค่า"""
    loss = ''
    for i in value:
        loss += str((int(i)+1)%2)
    print(loss.lstrip("0"))
number(input())
