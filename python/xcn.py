#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author: gaojunliang
Email: ggjjl1@126.com
Date: 2022-05-17
Description: 一个自动在freiexchange平台上挂单XCN的小程序
"""
import sys
import json
import requests
import time
import random

ticker = "https://api.freiexchange.com/public/ticker/XCN"
orderbook = "https://api.freiexchange.com/public/orderbook/XCN"
buy_url = "https://freiexchange.com/exchange/buy/XCN"
payload = {
    "csrf_test_name": "***",
    "price": "0.00000001",
    "amount": "1000",
}
# 临时cookie
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
    "cookie": "***",
}


def main():
    seed = int(random.random() * 10) % 5
    # 程序开始后，延时10秒执行
    exec_time = int(time.time()) + 10
    i = 10
    while i > 0:
        print(i)
        time.sleep(1)
        i = i - 1
    print("程序开始运行...")
    while True:
        payload["amount"] = str(random.randint(1000, 1500))
        seed = int(random.random() * 10) % 5
        now_time = int(time.time())
        print("now_time: %d, seed: %d" % (now_time, seed))
        if exec_time <= now_time:
            if seed != 1:
                exec_time += 300
                print("下一次执行时间：%d" % exec_time)
                continue
            r = requests.post(buy_url, data=payload, headers=headers)
            if json.loads(r.text)["message"] != "Order completed":
                print("订单提交出错！")
                sys.exit(-1)
            exec_time += 300
            print(payload)
            print(r.text)
            print("下一次执行时间：%d" % exec_time)
        else:
            # sleep 10秒
            time.sleep(10)


def test():
    payload["amount"] = str(random.randint(1000, 1500))
    r = requests.post(buy_url, data=payload, headers=headers)
    print(payload)
    print(r.text)
    print(json.loads(r.text)["message"])


if __name__ == "__main__":
    main()
