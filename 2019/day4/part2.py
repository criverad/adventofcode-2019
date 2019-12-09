def contains_adjacent_digits(pwd):
    for d in range(0, 10):
        two_digits = "%d%d" % (d, d)
        three_digits = "%d%d%d" % (d, d, d)
        if two_digits in pwd and three_digits not in pwd:
            return True
    return False

def contains_increasing_digits(pwd):
    for i in range(0, len(pwd) - 1):
        if (pwd[i] > pwd[i + 1]):
            return False
    return True

def is_potential(pwd):
    pwd_str = str(pwd)
    return contains_adjacent_digits(pwd_str) and contains_increasing_digits(pwd_str)

def passwords_meeting_criteria(start, end):
    all_pwds = range(start, end + 1)
    return [pwd for pwd in all_pwds if is_potential(pwd)]

print(len(passwords_meeting_criteria(125730, 579381)))
# print(passwords_meeting_criteria(111122, 111123))