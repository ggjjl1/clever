#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import requests

def get_block():
    payload = {
        'key1': 111,
    }
    r = requests.get('http://gao:gao123@localhost:8252', params=payload)


if __name__ == '__main__':
    print('\n')
    print('+---------------------+')
    print('| 日期：2021-07-14    |')
    print('| 作者：高俊亮        |')
    print('| 程序说明：测试测试  |')
    print('+---------------------+')
    print('\n')
    
    get_block()
