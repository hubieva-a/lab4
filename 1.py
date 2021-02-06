# Дано число. Вывести на экран название дня недели, который соответствует
# этому номеру.

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    n = input("Number of the day of the week")
    n = int(n)

    if n == 1:
        print("Monday")
    elif n== 2:
        print("Tuesday")
    elif n == 3:
        print("Wednesday")
    elif n == 4:
        print("Thursday")
    elif n == 5:
        print("Friday")
    elif n == 6:
        print("Saturday")
    elif n == 7:
        print("Sunday")
    else:
        print("Please choose a number in range from 1 to 7")
        exit(1)