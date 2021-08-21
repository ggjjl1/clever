#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests


def main():
    r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
    r.status_code


if __name__ == '__main__':
    main()
