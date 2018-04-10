import pymongo
import time

client = pymongo.MongoClient('localhost', 27017)
baidu = client['baidu']
data_sources = baidu['data_sources']  # 存储原始数据
link_details = baidu['link_details']  # 存储节目的具体信息

while True:
    print(link_details.find().count())
    time.sleep(5)
