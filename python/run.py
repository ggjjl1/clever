#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from datetime import datetime


def leap_year(year):
    """判断闰年"""
    if year % 4 == 0 \
            and (year % 100 != 0 or year % 400 == 0):
        return True

    return False


def main():
    if leap_year(2022):
        print("闰年")
    else:
        print("平年")


if __name__ == '__main__':
    main()
