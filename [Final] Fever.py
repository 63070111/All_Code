"""[Final] Fever"""
def cool(temperature):
    """หนาว"""
    if 36 <= temperature < 38:
        print("No Fever")
    elif 38 <= temperature < 39:
        print("Mild Fever")
    elif 39 <= temperature < 40:
        print("High Fever")
    else:
        print("Very High Fever")
cool(float(input()))

