# Напечатать три данных действительных числа , и сначала в порядке
# их возрастания,затем - в порядке убывания.

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    a = int(input("A = "))
    b = int(input("B = "))
    c = int(input("C = "))

    if a > b and a > c:
        if b > c:
            print(c, b, a)
            print(a, b, c)
        else:
            print(b, c, a)
            print(a, c, b)
    elif a > b and c> a:
        print(b, a, c)
        print(c, a, b)
    elif b > a and c > a and c > b:
        print(a, b, c)
        print(c, b, a)
        exit(1)
