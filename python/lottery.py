#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

def lottery():
    a = [i for i in range(1, 34)]
    b = [j for j in range(1, 16)]
    reds = sorted(random.sample(a, 6))
    blues = random.choice(b)
    return tuple(reds + [blues])

if __name__ == "__main__":
    # 双色球摇号模拟器，输出1000万个随机号码
    path = "C:\\Users\\admin\\Desktop\\numbers.txt"
    with open(path, 'w') as f:
        for i in range(10000000):
            answer = lottery()
            numbers = " ".join([str(x) if x > 9 else "0" + str(x) for x in answer]) + "\n"
            f.write(numbers)
    # print(answer)
    
    # answer = lottery()
    # numbers = " ".join([str(x) if x > 9 else "0" + str(x) for x in answer])
    # print(numbers)