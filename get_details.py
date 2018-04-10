import random
import requests
from bs4 import BeautifulSoup
import time
import pymongo
from fake_useragent import UserAgent

client = pymongo.MongoClient('localhost', 27017)
baidu = client['baidu']
data_sources = baidu['data_sources']  # 存储原始数据
link_details = baidu['link_details']  # 存储节目的具体信息
ua = UserAgent()


def get_details_function(name):
    headers = {
        'User-Agent': ua.random,
        'Connection': 'keep-alive',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7'
    }

    # http://cn-proxy.com/ 每天更新 需翻墙 暂时用Excel对付着
    proxy_list = [
        'http://39.134.10.15:8080',
        'http://39.134.10.25:8080',
        'http://39.134.10.22:8080',
        'http://39.134.10.11:8080',
        'http://39.134.10.27:8080',
        'http://39.134.10.101:8080',
        'http://39.134.10.13:8080',
        'http://39.134.10.17:8080',
        'http://39.134.10.21:8080',
        'http://39.134.10.100:8080',
        'http://39.134.10.14:8080',
        'http://39.134.10.5:8080',
        'http://193.112.1.24:3128',
        'http://39.134.10.20:8080',
        'http://39.134.10.18:8080',
        'http://39.134.10.24:8080',
        'http://39.134.10.23:8080',
        'http://39.134.10.6:8080',
        'http://39.134.10.99:8080',
        'http://39.134.10.98:8080',
        'http://39.134.10.2:8080',
        'http://39.134.10.3:8080',
        'http://39.134.10.10:8080'
    ]
    proxies = {
        'http': random.choice(proxy_list)
    }
    try:
        time.sleep(random.uniform(1, 3))  # 随机停顿1-3秒
        search_url = 'http://v.baidu.com/v?word={}{}'.format(name, '&ie=utf-8')
        res = requests.get(search_url, headers=headers, proxies=proxies, timeout=5)
        soup = BeautifulSoup(res.text, 'html.parser')
        programme = soup.select('h3 a.title')[0].get('title')
        # the_type = soup.select('li.type-tag.intro-item span:nth-of-type(2)')[0].text
        area = soup.select('li.intro-item span')
        # area = ['地区：', '内地\xa0\n', '类型：', '喜剧\xa0\n动画\xa0\n冒险\xa0\n', '别名：', '贝肯熊', '作者：', '林亚伦\n']
        area_text = 'null'
        type_text = 'null'
        array = []
        num = 0
        for i in area:
            num = num + 1
            if num < 9:
                array.append(i.text)
        # print(array)
        num2 = 0
        for my_data in array:
            num2 = num2 + 1
            if '地区' in my_data:
                area_text = array[num2].split()[0]
            if '类型' in my_data:
                type_text = '/'.join(array[num2].split())
        data = {
            'search_name': name,
            'got_name': programme,
            'type': type_text,
            'area': area_text
        }
        link_details.insert_one(data)
        print(name, programme, type_text, area_text)
    except Exception as e:
        print(search_url, 'error!', res.status_code)
        print(proxies)
        print(e)

# for data2 in data_sources.find().limit(10):
#     get_details_function(data2['name'])
