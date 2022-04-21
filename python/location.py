#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: gaojunliang
# date: 2021-08-24
# description: 根据经纬度获取地理位置信息，或者根据地理位置信息获取经纬度
import json
import requests

# 高德地图api
# 文档：https://lbs.amap.com/api/webservice/guide/api/georegeo
# 示例：https://restapi.amap.com/v3/geocode/regeo?location=116.310003,39.991957&key=<用户的key>&radius=100&extensions=base
regeo_url = "https://restapi.amap.com/v3/geocode/regeo"

geo_url = "https://restapi.amap.com/v3/geocode/geo"

# 需要申请自己的key
seckey = "******"


def lnglat_to_address(location):
    "经纬度转换为地理位置"
    # target_url = base_url + "?location=" + location + "&key=" + seckey + "&radius=100&extensions=base"
    payload = {
        'location': location,
        'key': seckey,
        'radius': 100,
        'extensions': 'base'
    }
    # print("请求url：" + target_url)
    r = requests.get(regeo_url, params=payload)
    json_obj = r.json()

    # 返回结构化地址信息
    address = json_obj['regeocode']['formatted_address']
    print(address)
    return address


def address_to_lnglat(address):
    "地理位置转换为经纬度"
    # target_url = base_url1 + '?address=' + address + '&key=' + seckey
    payload = {
        'address': address,
        'key': seckey
    }
    r = requests.get(geo_url, params=payload)
    obj = r.json()
    location = obj['geocodes'][0]['location']
    print(location)

    return location


def main():
    filename = '/Users/gaojunliang/Desktop/out.txt'
    data = []
    with open('/Users/gaojunliang/Desktop/post_location.txt', 'r') as f:
        for line in f:
            pid, location = line.replace('\n', '').split('\t')
            # print("pid:" + pid + ", location:" + location)
            address = lnglat_to_address(location)
            data.append((pid, location, address))

    # 写文件
    with open(filename, 'w') as f:
        for row in data:
            f.write(str(row[0]) + '\t' + row[1] + '\t' + str(row[2]) + '\n')


if __name__ == '__main__':
    # main()
    lnglat = address_to_lnglat('北京市海淀区中关村地铁站')
    print(lnglat)