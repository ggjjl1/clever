#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

url = 'https://freiexchange.com/'


def main():
    r = requests.get(url)
    print(r.status_code)


if __name__ == '__main__':
    main()
