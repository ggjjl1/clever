#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import redis
from datetime import datetime


class Clever(object):
    """clever核心代码"""

    def __init__(self, name):
        self.name = name


def leap_year(year):
    """判断闰年"""
    if year % 4 == 0 \
            and (year % 100 != 0 or year % 400 == 0):
        return True

    return False


def main():
    now = datetime.now()
    print("打印当前时间：%s" % now.strftime('%Y-%m-%d %H:%M:%S'))


if __name__ == '__main__':
    main()
