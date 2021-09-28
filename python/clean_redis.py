#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 功能：一个用来删除redis废弃key的脚本
import redis

r = redis.Redis(host='localhost', port=6379, db=0)

def clean_redis():
    for key in r.scan_iter(match='personasV4:uid:*', count=1):
        keyname = key.decode('utf-8')
        r.hdel(keyname, 'recent_create_chat_uids')
        print('删除key：' + keyname)

if __name__ == '__main__':
    clean_redis()
