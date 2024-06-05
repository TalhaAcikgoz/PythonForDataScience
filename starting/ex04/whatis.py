import sys as s

arg = s.argv
count = len(arg)

if count == 1:
    exit()

if count != 2:
    print("AssertionError: more than one argument is provided")
    exit()

try:
    n = int(arg[1])
    if n % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
except:
    print("AssertionError: argument is not an integer")