import pymongo
from pandas import DataFrame
from fake_useragent import UserAgent

client = pymongo.MongoClient('localhost', 27017)
baidu = client['baidu']
data_sources = baidu['data_sources']  # 存储原始数据
link_details = baidu['link_details']  # 存储节目的具体信息

array = [i for i in link_details.find({}, {'_id': 0})]
df = DataFrame(array)
df.to_excel('details.xlsx')


# ua = UserAgent()
#
#
# def get():
#     for i in range(1, 9):
#         print(ua.random)
#
#
# get()
