#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: gaojunliang
# date: 2021-08-25
# description: 尝试抓取一下豆瓣电影信息
import time
import requests
import mysql.connector

# 豆瓣首页url
douban_home_url = "https://www.douban.com/"

# 豆瓣首页电影分类标签列表
movie_tag_url_list = [
    "https://movie.douban.com/tag/爱情",
    "https://movie.douban.com/tag/剧情",
    "https://movie.douban.com/tag/喜剧",
    "https://movie.douban.com/tag/悬疑",
    "https://movie.douban.com/tag/经典",
    "https://movie.douban.com/tag/动画",
    "https://movie.douban.com/tag/科幻",
    "https://movie.douban.com/tag/犯罪",
    "https://movie.douban.com/tag/动作",
    "https://movie.douban.com/tag/青春",
    "https://movie.douban.com/tag/搞笑",
    "https://movie.douban.com/tag/文艺",
    "https://movie.douban.com/tag/惊悚",
    "https://movie.douban.com/tag/励志",
    "https://movie.douban.com/tag/纪录片",
    "https://movie.douban.com/tag/黑色幽默",
    "https://movie.douban.com/tag/战争",
    "https://movie.douban.com/tag/家庭",
    "https://movie.douban.com/tag/美国",
    "https://movie.douban.com/tag/日本",
    "https://movie.douban.com/tag/香港",
    "https://movie.douban.com/tag/中国大陆",
    "https://movie.douban.com/tag/韩国",
    "https://movie.douban.com/tag/中国",
    "https://movie.douban.com/tag/英国",
    "https://movie.douban.com/tag/法国",
    "https://movie.douban.com/tag/台湾",
    "https://movie.douban.com/tag/印度",
]

# 请求头user-agent
headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
}


def douban(url):
    # 连接mysql
    conn = mysql.connector.connect(
        host="127.0.0.1", user="root", password="12345678", database="douban"
    )
    cursor = conn.cursor()

    r = requests.get(url, headers=headers)
    obj = r.json()
    try:
        movies = obj["data"]
        print("电影数量：%d" % len(movies))
        for movie in movies:
            directors = movie["directors"]
            rate = movie["rate"]
            cover_x = movie["cover_x"]
            star = movie["star"]
            title = movie["title"]
            url = movie["url"]
            casts = movie["casts"]
            cover = movie["cover"]
            id = movie["id"]
            cover_y = movie["cover_y"]
            sql = 'insert into movie (directors,rate,cover_x,star,title,url,casts,cover,id,cover_y)\
                values("{}","{}",{},"{}","{}","{}","{}","{}","{}",{})'.format(
                directors, rate, cover_x, star, title, url, casts, cover, id, cover_y
            )
            # print(sql)
            cursor.execute(sql)
            conn.commit()

    except KeyError:
        # 频繁抓取会被ip会被禁
        print(obj)
        time.sleep(30)

    cursor.close()
    conn.close()


def mysql_connect(host, user, passwd, database):
    conn = mysql.connector.connect(
        host="127.0.0.1", user="root", password="12345678", database="douban"
    )
    cursor = conn.cursor()
    cursor.execute("select * form movie limit 10")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    conn.close()


def main():
    ajax_url = "https://movie.douban.com/j/new_search_subjects"
    start, genres = 0, "爱情"

    while True:
        url = (
            ajax_url
            + "?sort=T&range=0,10&tags=&start="
            + str(start)
            + "&genres="
            + genres
        )
        print(url)
        douban(url)

        # 每次获取20条电影信息
        start = start + 20

        # 睡眠2秒
        time.sleep(2)


if __name__ == "__main__":
    main()
