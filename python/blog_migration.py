#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import mysql.connector


def main():
    # 连接数据库
    db = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        passwd="123456",
        database="ggjjl1"
    )
    cursor = db.cursor()
    
    # 准备数据集
    val = []
    path = "D:\\workspace\\blog\\source\\_posts"
    file_list = os.listdir(path)
    for i in file_list:
        data = ""
        file_obj = []
        fp = os.path.join(path, i)
        with open(fp, 'r', encoding="utf-8") as f:
            while True:
                line = f.readline()
                if not line:
                    break
                if line.strip() == "---":
                    if data:
                        file_obj.append(data)
                        data = ""
                else:
                    data = data + line    
            if data:
                file_obj.append(data)
                
            if len(file_obj) == 2:
                title = file_obj[0].split("\n")[0][len("title: "):]
                date = file_obj[0].split("\n")[1][len("date: "):]
                tags = file_obj[0].split("\n")[2][len("tags: "):]
                body = file_obj[1]
            elif len(file_obj) == 1:
                title = file_obj[0].split("\n")[0][len("title: "):]
                date = file_obj[0].split("\n")[1][len("date: "):]
                tags = file_obj[0].split("\n")[2][len("tags: "):]
                body = ""
            else:
                print(i)
                return
                
            # 去除标题转义字符
            title = title.replace("\\", "")
            
            val.append((title, date, tags, body))
    
    val.sort(key=lambda e:e[1])
    
    sql = "INSERT INTO post (author_id, title, create_time, tags, body, update_time) VALUES (1, %s, %s, %s, %s, now())"
    cursor.executemany(sql, val)
    db.commit()
    
    print(cursor.rowcount, "row inserted.")
    print("finished!")
    
    
if __name__ == "__main__":
    main()
