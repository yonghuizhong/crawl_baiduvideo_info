import pymongo
import time
import sys
import os


client = pymongo.MongoClient('localhost', 27017)
baidu = client['baidu']
data_sources = baidu['data_sources']  # 存储原始数据
link_details = baidu['link_details']  # 存储节目的具体信息


# def restart_program():
#     python = sys.executable
#     print(python)
#     os.execl(python, python, *sys.argv)

count = 0  # test.py执行次数


def watch():
    global count    # 定义全局变量
    while True:
        count = count + 1
        data_array = [i['name'] for i in data_sources.find()]  # 数据库的原始数据
        got_array = [i['search_name'] for i in link_details.find()]  # 已经爬到的数据
        x = set(data_array)
        y = set(got_array)
        rest_array = x.difference(y)  # 需要爬的数据
        print(len(x), len(y), len(rest_array))
        if len(rest_array) > 0 and count < 10:
            if count == 1:
                print('第', count, '次运行程序')
                os.system('python test.py')
            else:
                print('第', count, '次运行程序')
                print('暂停30秒...')
                time.sleep(30)
                os.system('python test.py')
        else:
            print('爬虫重启次数达到限值，已停止；或已经爬取完毕~')
            sys.exit()


watch()



