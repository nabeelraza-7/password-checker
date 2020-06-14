#! python
#This is my first repository to practice using github
import sys

if len(sys.argv) == 0:
    print("Enter the password next to the file name.")
else:
    password = "".join(sys.argv[1:])
    print(password)
    tests_failed = {}
    symbols = "!@#$%^&*~><?|.,'\""
    for i in symbols:
        if i in password:
            break
    else:
        tests_failed["symbols"] = False
    if len(password) < 8:
        tests_failed["length"] =  False
    numbers = "1234567890"
    for i in numbers:
        if i in password:
            break
    else:
        tests_failed["numbers"] = False
    letters = "abcdefghijklmnopqrstuvwxyz"
    for i in letters:
        if i in password or i.upper() in password:
            break
    else:
        tests_failed["letters"] = False
    print(tests_failed)
    for i,j in tests_failed.items():
        if not j:
            if i == 'symbols':
                print("Need symbols in the password!")
            if i == 'length':
                print("The length of the password is shorter than 8!")
            if i == 'numbers':
                print("No numbers found in the password!")
            if i == 'letters':
                print("No letters found in the password!")
        