"""[Midterm] ValidVar"""
import string
punc_list = string.punctuation.replace('_', "")
number = int(input())

def check_name(name):
    if name in ['if', 'else', 'elif', 'while', 'for', 'True', 'False', 'continue', 'break',
                'return', 'is', 'in', 'and', 'or', 'from', 'pass', 'not', 'def', 'None'] or \
            name[0].isdigit() or \
            " " in name or \
            any(punc in name for punc in punc_list):
        return False
    return True

validity_list = []
for i in range(number):
    name = input()
    validity_list.append(check_name(name.strip()))

for valid in validity_list:
    if valid:
        print('Valid')
    else:
        print('Invalid')
