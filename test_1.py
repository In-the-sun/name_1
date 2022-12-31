# coding=utf-8
# “大数据”、“人工智能”、“计算机”为关键字
# 第一页
# 采集的岗位信息，包括：招聘专业、岗位工作、薪资、工作地点等不少于10个特征信息
import numpy as np
import requests
from selenium import webdriver
from lxml import etree
import pandas as pd
import time

driver = webdriver.Chrome()  # 启动chrome浏览器
url = 'https://www.zhipin.com/web/geek/job?query=%E5%A4%A7%E6%95%B0%E6%8D%AE%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD%E8' \
      '%AE%A1%E7%AE%97%E6%9C%BA&city=100010000 '
driver.get(url)  # 获取网页源码数据

dom_web = etree.HTML(driver.page_source)

job_name = dom_web.xpath('//div[@id="wrap"]//div[@class="job-title clearfix"]/span[@class="job-name"]/text()')
job_area = dom_web.xpath('//div[@id="wrap"]//div[@class="job-title clearfix"]//span[@class="job-area"]/text()')
salary = dom_web.xpath('//div[@id="wrap"]//div[@class="job-info clearfix"]/span[@class="salary"]/text()')
# deal = dom_web.xpath('//div[@id="wrap"]//div[@class="job-card-footer clearfix"]/div/text()')
# basic_need = dom_web.xpath('//div[@id="wrap"]//div[@class="job-info clearfix"]/ul[@class="tag-list"]/li/text()')
# skill = dom_web.xpath('//div[@id="wrap"]//div[@class="job-card-footer clearfix"]/ul[@class="tag-list"]/li/text()')
corporation_name = dom_web.xpath('//div[@id="wrap"]//div[@class="job-card-right"]//h3[@class="company-name"]/a/text()')
# corporation_basic_information = dom_web.xpath('//div[@id="wrap"]//div[@class="job-card-right"]//ul[@class="company-tag-list"]/li/text()')

# list_1 = [job_name, job_area, salary, deal, basic_need, skill, corporation_name, corporation_basic_information]
# list_1 = [job_name, job_area, salary, corporation_name]
# data_1 = pd.DataFrame(list_1).T
data_1 = pd.DataFrame({'工作名称': job_name, '工作地点': job_area, '薪资': salary, '公司名称': corporation_name})

usr_url = dom_web.xpath('//div[@id="wrap"]//div[@class="job-card-body clearfix"]/a/@href')
print(usr_url)

# cookies_str = 'wd_guid=8416904d-8e0a-4630-90ee-50c1948e34c5; historyState=state; lastCity=100010000; _bl_uid=7dlyhbFOv33wphz6L4dkeIm40mUm; sid=sem_pz_bdpc_dasou_title; __g=sem_pz_bdpc_dasou_title; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1671497493,1671521860,1671588696; __l=l=%2Fwww.zhipin.com%2Fweb%2Fgeek%2Fjob%3Fquery%3D%25E5%25A4%25A7%25E6%2595%25B0%25E6%258D%25AE%25E4%25BA%25BA%25E5%25B7%25A5%25E6%2599%25BA%25E8%2583%25BD%25E8%25AE%25A1%25E7%25AE%2597%25E6%259C%25BA%26city%3D100010000&r=https%3A%2F%2Fwww.baidu.com%2Fother.php%3Fsc.K00000Kz-sEM2gi-pCvfl1EjO6SSguFCKRj50drT2WwIVxfHOQRtNRbCCL17AchxHauOY_JgS0APFblrhAER99B2-6JbkOe3g5zt0rfz3ncLjzsipTqPunmVfKLvBo70rbJdvoy7oOu8vNzGEHcsAp0LXMc021-KlZmAKu531neq_04V34xCSj9xqCRo_pMsIZDcjWRR3L771W6VTfX3T9ax69sa.7D_NR2Ar5Od663rj6t8AGSPticrtXFBPrM-kt5QxIW94UhmLmry6S9wiGyAp7BEIu80.TLFWgv-b5HDkrfK1ThPGujYknHb0THY0IAYqmhq1Tqpkko60IgP-T-qYXgK-5H00mywxIZ-suHY10ZIEThfqmhq1Tqpkko60ThPv5H00IgF_gv-b5HDdPjD1PjT4nWm0UgNxpyfqnHRsPWRYnWc0UNqGujYknH64njcsn0KVIZK_gv-b5HDzrjcv0ZKvgv-b5H00pywW5R9rffKspyfqrfKWpyfqnHfz0APzm1YdPHcLrf%26dt%3D1671588693%26wd%3Dboss%25E7%259B%25B4%25E8%2581%2598%26tpl%3Dtpl_12826_30685_0%26l%3D1541347926%26us%3DlinkVersion%253D1%2526compPath%253D10036.0-10032.0%2526label%253D%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkType%253D%2526linkText%253DBOSS%2525E7%25259B%2525B4%2525E8%252581%252598%2525E2%252580%252594%2525E2%252580%252594%2525E6%252589%2525BE%2525E5%2525B7%2525A5%2525E4%2525BD%25259C%2525EF%2525BC%25258C%2525E4%2525B8%25258ABOSS%2525E7%25259B%2525B4%2525E8%252581%252598%2525EF%2525BC%25258C&g=%2Fwww.zhipin.com%2F%3Fsid%3Dsem_pz_bdpc_dasou_title&s=3&friend_source=0&s=3&friend_source=0; __c=1671588695; __a=37168116.1671497492.1671521860.1671588695.35.3.3.3; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1671588706; __zp_stoken__=f447eXWt6M2t%2FRRMpYxdUX2duCXdFMhpVb01ubzAgYC97bGcjJlpwaS9JMl5zBVJvOx8TLylKfyAyTh8vYQ4rID0ZdjBgfno1Gld1R2ETSC94M1M3f1dmcWVrLz0FHFYldmUGNSVOcBV3Qx4CDi56OjVbPxkJIVFaQXQzd1h7UUUwGCtWPhFZA0k0RzVHJWRELRt2TXJ%2BdA%3D%3D'
# cookies = {}
# for i in cookies_str.split(';'):  # 将cookies整理成所需格式
#     k, v = i.split('=', 1)
#     cookies[k] = v
#
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
# }  # 设置请求头

list_2 = []
list_3 = []
for i in usr_url:
    t = 5 + np.random.random()
    url = 'https://www.zhipin.com' + i
    print(url)
    while True:
        print("-")
        t = t + 1
        # web_data = requests.get(url, cookies=cookies, headers=headers)
        driver.get(url)
        dom_web = etree.HTML(driver.page_source)
        job_description = dom_web.xpath('//div[@class="job-sec-text"]/text()')
        job_description = ' '.join(job_description)
        corporation_description = dom_web.xpath('//div[@class="job-sec-text fold-text"]/text()')
        corporation_description = ' '.join(corporation_description)
        if len(job_description):
            break
        time.sleep(t)
    list_2.append(job_description)
    list_3.append(corporation_description)
    time.sleep(t)
data_2 = pd.DataFrame({'职位描述': list_2})
data_3 = pd.DataFrame({'公司介绍': list_3})
data = pd.concat([data_1, data_2, data_3], axis=1)

data.to_csv('boss数据_2.csv', index=None, encoding='utf-8-sig')
