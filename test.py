import pymongo
import sys
import os
from multiprocessing import Pool

import time

from get_details import get_details_function

client = pymongo.MongoClient('localhost', 27017)
baidu = client['baidu']
data_sources = baidu['data_sources']  # 存储原始数据
link_details = baidu['link_details']  # 存储节目的具体信息

data_array = [i['name'] for i in data_sources.find()]  # 数据库的原始数据
got_array = [i['search_name'] for i in link_details.find()]  # 已经爬到的数据
x = set(data_array)
y = set(got_array)
rest_array = x.difference(y)  # 需要爬的数据
print(len(x), len(y), len(rest_array))


if __name__ == '__main__':
    pool = Pool()
    pool.map(get_details_function, rest_array)
