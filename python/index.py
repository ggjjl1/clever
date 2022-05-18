#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
英语单词查询
"""

# 大学英语四级词库
path = "/Users/gaojunliang/workspace/english-wordlists/CET4_edited.txt"


def search(*args, **kwargs):
    """单词查询"""
    keyword = kwargs["keyword"]
    index = 0
    with open(path, "r") as f:
        for line in f:
            index += 1
            word_group = line.strip().split(" ")
            if word_group[0].islower():
                if word_group[0] == keyword:
                    return word_group


if __name__ == "__main__":
    print(search(keyword="law"))
