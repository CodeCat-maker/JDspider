# -*- coding: utf-8 -*-
# @Time : 2020-11-18 22:35 
# @Author : CodeCat 
# @File : test.py
import xlwt

dblists = [
['康佳KKTV K48F1 48英寸三星屏幕 华为海思芯片 34核处理器 教育电视 智慧投屏 人工智能语音电视', '自营', '1699.00', ('4年全保修', '￥79.00'), ('5年全保修', '￥99.00'), ('6年全保修', '￥113.52')],
['三星（SAMSUNG）55英寸 TU8800 4K超高清 HDR 超薄AI智能客厅电视 教育资源液晶电视机UA55TU8800JXXZ', '自营', '5000.00', ('4年全保修', '￥209.00'), ('5年全保修', '￥279.00'), ('6年全保修', '￥298.32')],
['飞利浦 65英寸 4K全面屏 教育电视 HDR 独立音腔 AI语音 2级能效 海量应用 网络液晶智能电视65PUF7294/T3', '自营', '4299.00', ('4年全保修', '￥209.00'), ('5年全保修', '￥279.00'), ('6年全保修', '￥298.32')]
]


book = xlwt.Workbook(encoding='utf-8', style_compression=0)
sheet = book.add_sheet('电器', cell_overwrite_ok=True)
col = ("商品名称", "是否自营", "价格", "保障服务1", "保障服务2", "保障服务3")
for (i,j) in zip(dblists,range(0,len(dblists))):
    print(i,j)