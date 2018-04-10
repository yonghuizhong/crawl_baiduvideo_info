import json
import pymongo
import xlrd as xlrd

client = pymongo.MongoClient('localhost', 27017)
baidu = client['baidu']
data_sources = baidu['data_sources']  # 存储原始数据
link_details = baidu['link_details']  # 存储节目的具体信息


def my_data_sources():
    data = xlrd.open_workbook('name.xlsx')  # 读入数据
    table = data.sheets()[0]
    rowstag = table.row_values(0)  # 读取excel第一行数据作为存入mongodb的字段名
    nrows = table.nrows  # 得到行数
    # print(nrows)
    returnData = {}
    for i in range(1, nrows):
        # 将字段名和excel数据存储为字典形式，并转换为json格式
        returnData[i] = json.dumps(dict(zip(rowstag, table.row_values(i))))
        # 通过编解码还原数据
        returnData[i] = json.loads(returnData[i])
        # print(returnData[i])
        data_sources.insert(returnData[i])


# my_data_sources()
