# Одноклеточная амеба каждые три часа делится на 2 клетки. Определить, сколько будет
# клеток через 6 часов.

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    k = 1
    n = 1
    for k in range(1, n + 2):
        k = k*2
    print("Амеба поделится на столько клеток: " + str(k))
