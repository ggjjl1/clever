#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

if __name__ == "__main__":
    # python执行1.5亿次循环耗时时间
    counter = 0
    start = int(time.time() * 1000)
    for i in range(150000000):
        counter = counter + 1

    end = int(time.time() * 1000)
    print("执行时间：" + str(end - start) + "毫秒")
