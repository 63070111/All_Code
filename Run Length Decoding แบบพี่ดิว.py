"""Run Length Decoding"""
string = input()
new_string = ""
for i, word in enumerate(string):
    if i % 2 == 0:
        for j in range(int(string[i])):
            new_string += string[i + 1]

print(new_string)
