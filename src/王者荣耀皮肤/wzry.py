import datetime
import os
import requests

'''
王者荣耀皮肤下载
'''
url = 'https://pvp.qq.com/web201605/js/herolist.json'
hero_list = requests.get(url)  # 获取英雄列表json文件

hero_list_json = hero_list.json()  # 转化为json格式
# print(hero_list_json)
hero_name = list(map(lambda x: x['cname'], hero_list_json))  # 提取英雄的名字
# print(hero_name)
hero_number = list(map(lambda x: x['ename'], hero_list_json))  # 提取英雄的编号


# print(hero_number)


# 下载图片
def download_image():
    i = 0
    for j in hero_number:
        # 创建文件夹
        os.mkdir("D:\\wzry\\" + hero_name[i])
        # 进入创建好的文件夹
        os.chdir("D:\\wzry\\" + hero_name[i])
        i += 1
        for k in range(10):
            # 拼接url
            # http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/111/111-bigskin-1.jpg
            one_hero_link = 'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/' + str(j) + '/' + str(
                j) + '-pigskin-' + str(k) + '.jpg'
            im = requests.get(one_hero_link)  # 请求url
            if im.status_code == 200:
                open(str(k) + '.jpg', 'wb').write(im.content)  # 写入文件


curr_time = datetime.datetime.now()

download_image()

curr_time2 = datetime.datetime.now()
print(curr_time2 - curr_time)
