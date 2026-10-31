def password_check(check):
    lower, upper, digit, punc = 0,0,0,0
    for i in check:
        if i.islower():
            lower += 1
        elif i.isupper():
            upper += 1
        elif i.isdigit():
            digit += 1
        else:
            punc += 1
    if punc > 0 and lower > 0 and upper > 0 and digit > 0:
        print("Password secure")
    else:
        print("Password not secure")            

