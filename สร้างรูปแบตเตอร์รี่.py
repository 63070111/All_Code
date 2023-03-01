"""Battery Ver.1"""
def main():
    """แสดงค่า"""
    bat = int(input())
    bat_wide = int(input())
    number1 = (bat*bat_wide)//100
    number2 = bat_wide-number1
    text_o = "O"
    text__ = "_"
    print("(%s%s) %d%%"%(text_o*number1, text__*number2, bat))
main()




