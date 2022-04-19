#!/usr/bin/env python
# -*- coding: utf-8 -*-

def fib(n):
    a, b = 0, 1
    nums = []
    for i in range(0, n + 1):
        nums.append(str(a))
        a, b = b, a + b
    return nums

if __name__ == '__main__':
    nums = fib(100)
    print('%s%s%s' % ('[',','.join(nums),']'))
