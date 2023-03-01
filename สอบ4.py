"""dek64"""
def get_admission(faculty, score):
    """64"""
    if faculty == 'ENG':
        return score >= 21000
    elif faculty == 'IT':
        return score >= 16000
    elif faculty == 'ARCH':
        return score >= 23000
    elif faculty == 'ART':
        return score >= 18650
    elif faculty == 'EDU':
        return score >= 19000
    elif faculty == 'ATECH':
        return score >= 15000
    elif faculty == 'AIND':
        return score >= 17750
    elif faculty == 'SCI':
        return score >= 20550
    elif faculty == 'NSCI':
        return score >= 20450
    elif faculty == 'A&M':
        return score >= 16750
    elif faculty == 'PILOT':
        return score >= 22220
    elif faculty == 'MED':
        return score >= 24000
    else:
        return False
def main():
    """เย้"""
    score = int(input())
    faculty_1 = input()
    faculty_2 = input()
    faculty_3 = input()
    faculty_4 = input()
    faculty_5 = input()
    if score > 30000:
        print('Error! Please try again.')
        return
    if get_admission(faculty_1, score):
        print(faculty_1)
        return
    score -= 250
    if get_admission(faculty_2, score):
        print(faculty_2)
        return
    score -= 500
    if get_admission(faculty_3, score):
        print(faculty_3)
        return
    score -= 1000
    if get_admission(faculty_4, score):
        print(faculty_4)
        return
    score -= 2000
    if get_admission(faculty_5, score):
        print(faculty_5)
        return
    print("See ya next year!")
main()




