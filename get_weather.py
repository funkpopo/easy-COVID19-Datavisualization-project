# -*_ coding:UTF-8 -*-
import requests
from lxml import etree
from openpyxl import workbook  # 写入Excel表所用
from openpyxl import load_workbook  # 读取Excel表所用

url = "http://www.tianqihoubao.com/lishi/kunming/month/202001.html"
response = requests.get(url)
response.encoding = 'gbk'
html = response.text

tree = etree.HTML(response.content)
table = tree.xpath("//table//tr[position()>=1]")

wb = workbook.Workbook()  # 创建Excel对象
ws = wb.active  # 获取当前正在操作的表对象
ws.append(['date', 'tmp', 'weather']) # 文件标题

for i in table:  # 遍历tr列表
    # 获取当前tr标签下的第一个td标签，并用text()方法获取文本内容，赋值给p
    p2 = ''.join(i.xpath(".//td[1]//text()")) # date
    p3 = ''.join(i.xpath(".//td[2]//text()")) # tmp
    p4 = ''.join(i.xpath(".//td[3]//text()")) # weather

    # 往表中写入标题行,以列表形式写入！
    ws.append([p2, p3, p4])

    data = {
        'date': ''.join(p2.split()),
        'tmp': ''.join(p3.split()),
        'weather': ''.join(p4.split())
    }
    print(data)
