import string
import random
def creation(pass_len):
    li = []
    password = []
    for i in string.ascii_letters:
        li.append(i)
    for i in string.punctuation:
        li.append(i)
    for i in string.digits:
        li.append(i)
    for i in range(pass_len):
        password.append(random.choice(li))
    print("The password generated: ")
    return "".join(password)
