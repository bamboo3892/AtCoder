import string
import math
import numpy as np


ALPH = list(string.ascii_lowercase)
ALPH = {ALPH[i]: i for i in range(len(ALPH))}


def main():
    s1 = input()
    s2 = input()
    s3 = input()

    non_zero = [s1[0], s2[0], s3[0]]
    allocaton = [None] * 10
    provided = [None] * len(ALPH)

    result = fun1(s1, s2, s3, 0, allocaton, provided, non_zero)

    if(result):
        ss1 = ""
        ss2 = ""
        ss3 = ""
        for i in range(len(s1)):
            ss1 += str(provided[ALPH[s1[i]]])
        for i in range(len(s2)):
            ss2 += str(provided[ALPH[s2[i]]])
        for i in range(len(s3)):
            ss3 += str(provided[ALPH[s3[i]]])
        print(ss1)
        print(ss2)
        print(ss3)
    else:
        print("UNSOLVABLE")


def fun1(s1, s2, s3, carry, allocaton, provided, non_zero):
    no_loop = False
    if(s1 == ""):
        no_loop = True
    elif(provided[ALPH[s1[-1]]] is not None):
        carry += provided[ALPH[s1[-1]]]
        no_loop = True

    if(no_loop):
        return func2(s1, s2, s3, carry, allocaton, provided, non_zero)
    else:
        for i in range(10):
            if(i == 0 and s1[-1] in non_zero):
                continue
            if(allocaton[i] is None):
                allocaton[i] = s1[-1]
                provided[ALPH[s1[-1]]] = i
                carry += i
                result = func2(s1, s2, s3, carry, allocaton, provided, non_zero)
                if(result):
                    return True
                else:
                    allocaton[i] = None
                    provided[ALPH[s1[-1]]] = None
                    carry -= i
        return False


def func2(s1, s2, s3, carry, allocaton, provided, non_zero):
    no_loop = False
    if(s2 == ""):
        no_loop = True
    elif(provided[ALPH[s2[-1]]] is not None):
        carry += provided[ALPH[s2[-1]]]
        no_loop = True

    if(no_loop):
        return func3(s1, s2, s3, carry, allocaton, provided, non_zero)
    else:
        for i in range(10):
            if(i == 0 and s2[-1] in non_zero):
                continue
            if(allocaton[i] is None):
                allocaton[i] = s2[-1]
                provided[ALPH[s2[-1]]] = i
                carry += i
                result = func3(s1, s2, s3, carry, allocaton, provided, non_zero)
                if(result):
                    return True
                else:
                    allocaton[i] = None
                    provided[ALPH[s2[-1]]] = None
                    carry -= i
        return False


def func3(s1, s2, s3, carry, allocaton, provided, non_zero):
    no_loop = False
    if(s3 == ""):
        no_loop = True
    elif(provided[ALPH[s3[-1]]] is not None):
        carry -= provided[ALPH[s3[-1]]]
        no_loop = True

    if(no_loop):
        return next_digit(s1, s2, s3, carry, allocaton, provided, non_zero)
    else:
        for i in range(10):
            if(i == 0 and s3[-1] in non_zero):
                continue
            if(allocaton[i] is None):
                allocaton[i] = s3[-1]
                provided[ALPH[s3[-1]]] = i
                carry -= i
                result = next_digit(s1, s2, s3, carry, allocaton, provided, non_zero)
                if(result):
                    return True
                else:
                    allocaton[i] = None
                    provided[ALPH[s3[-1]]] = None
                    carry += i
        return False


def next_digit(s1, s2, s3, carry, allocaton, provided, non_zero):
    if(max([len(s1), len(s2), len(s3)]) == 1):
        return carry == 0
    else:
        if(carry % 10 == 0):
            return fun1(s1[:-1], s2[:-1], s3[:-1], carry // 10, allocaton, provided, non_zero)
        else:
            return False


if(__name__ == "__main__"):
    main()
