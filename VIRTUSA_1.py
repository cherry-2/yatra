# Write a program which takes two strings as input from the user (str1 and str2). This program should print two strings as output (op1 and op2).
# op1 should contain all the characters which are present in str1 but NOT present in str2.
# op2 should contain all the characters which are present in str2 but NOT present in str1.

def UncommonInsStr1():
    str1 = input(str("enter the str1:"))
    str2 = input(str("enter the str2:"))
    a = set(str1)
    b = set(str2)
    c = a.intersection(b)
    str3 = a.difference(c)
    op1 = str(str3)
    print("op1:", op1)
    str4 = b.difference(c)
    op2 = str(str4)
    if op2 != set():
        print("op2:", op2)
    else:
        print("op2: null")


UncommonInsStr1()
