"""Battery Ver.1 new"""
def main():
    """show me"""
    batly = int(input())
    bat_wide = 10
    number1 = (batly*bat_wide)//100
    number2 = bat_wide-number1
    text_o = "O"
    text__ = "_"
    print("(%s%s) %d%%"%(text_o*number1, text__*number2, batly))
main()
