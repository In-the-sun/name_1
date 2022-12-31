# coding=utf-8
# “大数据”、“人工智能”、“计算机”为关键字
# 多页
# 采集的岗位信息，包括：招聘专业、岗位工作、薪资、工作地点等不少于10个特征信息
import csv
import numpy as np
from selenium import webdriver
from lxml import etree
import pandas as pd
import time

driver = webdriver.Chrome()  # 启动chrome浏览器
url = 'https://www.zhipin.com/web/geek/job?query=%E5%A4%A7%E6%95%B0%E6%8D%AE%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD%E8' \
      '%AE%A1%E7%AE%97%E6%9C%BA&city=100010000 '
# driver.get(url)  # 获取网页源码数据


# dom_web = etree.HTML(driver.page_source)

headers = ["工作名称", "工作地点", "薪资", "公司名称", "职位描述", "公司介绍"]

with open('多页boss数据_1.csv', 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(headers)

# def get_external_data(i):
#     while True:
#         driver.get(url)  # 获取网页源码数据
#         dom_web = etree.HTML(driver.page_source)  # 网页源码解析，得到一个dom文件
#         job_name = dom_web.xpath('//div[@id="wrap"]//div[@class="job-title clearfix"]/span[@class="job-name"]/text()')
#         if len(job_name):
#             break
#         print("获取第",i,"页 失败")
#     job_area = dom_web.xpath('//div[@id="wrap"]//div[@class="job-title clearfix"]//span[@class="job-area"]/text()')
#     salary = dom_web.xpath('//div[@id="wrap"]//div[@class="job-info clearfix"]/span[@class="salary"]/text()')
#     corporation_name = dom_web.xpath(
#         '//div[@id="wrap"]//div[@class="job-card-right"]//h3[@class="company-name"]/a/text()')
#     usr_url = dom_web.xpath('//div[@id="wrap"]//div[@class="job-card-body clearfix"]/a/@href')
#     print(usr_url)
#     list_1 = [job_name, job_area, salary, corporation_name]
#     data_1 = pd.DataFrame(list_1).T

# def get_usr_data(usr_url):
#     list_2 = []
#     list_3 = []
#     for j in usr_url:
#         t = 5 + np.random.random()
#         url = 'https://www.zhipin.com' + j
#         print(url)
#         while True:
#             print("-")
#             t = t + 1
#             driver.get(url)
#             dom_user = etree.HTML(driver.page_source)
#             job_description = dom_user.xpath('//div[@class="job-sec-text"]/text()')
#             job_description = ' '.join(job_description)
#             corporation_description = dom_user.xpath('//div[@class="job-sec-text fold-text"]/text()')
#             corporation_description = ' '.join(corporation_description)
#             if len(job_description):
#                 break
#             time.sleep(t)
#         list_2.append(job_description)
#         list_3.append(corporation_description)
#         time.sleep(t)
#     data_2 = pd.DataFrame(list_2)
#     data_3 = pd.DataFrame(list_3)


for i in range(1, 11):
    # 获取一级页面数据
    url = 'https://www.zhipin.com/web/geek/job?query=%E5%A4%A7%E6%95%B0%E6%8D%AE%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD%E8' \
          f'%AE%A1%E7%AE%97%E6%9C%BA&city=100010000&page={i} '
    while True:
        driver.get(url)  # 获取网页源码数据

        time.sleep(10 + np.random.random())

        dom_web = etree.HTML(driver.page_source)  # 网页源码解析，得到一个dom文件
        job_name = dom_web.xpath('//div[@id="wrap"]//div[@class="job-title clearfix"]/span[@class="job-name"]/text()')
        if len(job_name):
            break
        print("获取第", i, "页 失败")
    job_area = dom_web.xpath('//div[@id="wrap"]//div[@class="job-title clearfix"]//span[@class="job-area"]/text()')
    salary = dom_web.xpath('//div[@id="wrap"]//div[@class="job-info clearfix"]/span[@class="salary"]/text()')
    corporation_name = dom_web.xpath(
        '//div[@id="wrap"]//div[@class="job-card-right"]//h3[@class="company-name"]/a/text()')
    all_usr_url = dom_web.xpath('//div[@id="wrap"]//div[@class="job-card-body clearfix"]/a/@href')
    print(all_usr_url)
    list_1 = [job_name, job_area, salary, corporation_name]
    data_1 = pd.DataFrame(list_1).T

    # 获取二级页面数据
    list_2 = []
    list_3 = []
    for j in all_usr_url:
        t = 5 + np.random.random()
        user_url = 'https://www.zhipin.com' + j
        print(user_url)
        while True:
            print("-")
            t = t + 1
            driver.get(user_url)
            time.sleep(t)
            dom_user = etree.HTML(driver.page_source)
            job_description = dom_user.xpath('//div[@class="job-sec-text"]/text()')
            job_description = ' '.join(job_description)
            corporation_description = dom_user.xpath('//div[@class="job-sec-text fold-text"]/text()')
            corporation_description = ' '.join(corporation_description)
            if len(job_description):
                break
            time.sleep(t)
        list_2.append(job_description)
        list_3.append(corporation_description)
    data_2 = pd.DataFrame(list_2)
    data_3 = pd.DataFrame(list_3)

    data = pd.concat([data_1, data_2, data_3], axis=1)
    data.to_csv('多页boss数据_1.csv', mode='a+', index=False, encoding='utf-8-sig', header=False)
