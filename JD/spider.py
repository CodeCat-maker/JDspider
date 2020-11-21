# -*- coding: utf-8 -*-
# @Time : 2020-11-18 11:15 
# @Author : CodeCat 
# @File : spider.py
import httpx,re,json,urllib.parse,xlwt,time
keyword = "家用电器 电视"
from bs4 import BeautifulSoup
dblists = []
def getmidstring(html, start_str, end):
    start = html.find(start_str)
    if start >= 0:
        start += len(start_str)
        end = html.find(end, start)
        if end >= 0:
            return html[start:end].strip()

def get_list(n):
    # a=time.time()
    # b = '%.5f' % a
    #url = 'https://search.jd.com/Search?keyword='+keyword+'&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E6%89%8B%E6%9C%BA&cid2=653&cid3=655&page=' + str(2 * n) + '&s=' + str(56 * n - 20) + '&scrolling=y&log_id=' + str(b)

    url = 'https://search.jd.com/Search?keyword='+keyword+'&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E7%94%B5%E8%84%91&page='+str(n)
    head = {'authority': 'search.jd.com',
            'method': 'GET',
            'path': '/s_new.php?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E6%89%8B%E6%9C%BA',
            'scheme': 'https',
            'referer': 'https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E6%89%8B%E6%9C%BA&cid2=653&cid3=655&page=3&s=58&click=0',
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
            'Cookie': 'shshshfpa=7ce3533c-d13a-e725-e791-42f3e155dd8e-1602338832; shshshfpb=sd3zEo4rdjJ3C6CIpxCv4Mg%3D%3D; unpl=V2_ZzNtbUJXFkJ1DE8HfUsPBmICRgoSU0occg5BBn0cWANnA0YKclRCFnQURlRnGVwUZwQZX0pcQRxFCEZkexhdBWIAF1RDUHMldQlHVXsdWwdgBSJeQmdCJXUPR1d5G1UMZAUbXkZXRBV2AEdTfx5sNWcLFW1CVkIUdQ9HVn4bVQxXMxNtQ2dDHHAPR1B9HFoMV0h8XA9XRBR2CkRdchpaDGQHElpCVEsUcgxBZHopXw%3d%3d; __jdv=76161171|baidu|-|organic|not set|1605666470329; PCSYCityID=CN_120000_120100_120111; areaId=3; user-key=c4f2668b-6050-4d15-a49c-be451b303a4f; ipLoc-djd=3-51045-55800-0; qrsc=3; pinId=HlSFKRDNdoAmEADFGq3gVrV9-x-f3wj7; pin=jd_5e042df8a26fc; unick=Anjor-on; _tp=8R%2F4Cbsgy6rsjyksIPyfFN1EwCkPodjtFU9nY4%2BoJTE%3D; _pst=jd_5e042df8a26fc; TrackID=1XVyGig-TSN_ynypJcH8gVNIXLd997oF-Dld_8UCHvCfchkiBXl8cSzNmQn5PIRwqvqv8TPNIwuKvPj5Mlt5h_GceYPgkGMnaeT5cZ5CmVeg; thor=197D0CAF33BCA29836F5B90FC2A717974D2A698337BC24FF0C6EDAB1A02DEED14D14D7FC4104AA1C9B9971599F1883D29791CD7AB3D3FEF3CAE5EA81A6468085427FC001C17F92AF8E1EC0EB8AED1FC3E8461BA237CC4340D1EE65E5495DDFCC81D6EF1592E6373DBD15970B33E9CA3F236D67039D9B61EE63BC3810544849E230234982F67F2C04541C045BFFE8A8ED814283909EA324D9C9D1275C64161DE3; ceshi3.com=201; __jda=76161171.1602338827825161290656.1602338827.1605700797.1605959451.11; __jdc=76161171; cn=6; __jdb=76161171.7.1602338827825161290656|11.1605959451; shshshfp=5303ca913f34465d687b17bbf38f3c01; shshshsID=41080a65ab88f38827096c8c583c379d_5_1605959541059'

            }
    html = httpx.get(url,headers=head).text
    soup = BeautifulSoup(html,'html.parser')
    good_list = soup.find_all('li',class_="gl-item")

    re_good = re.compile(r'<li class="gl-item" data-sku="(.*?)"')
    good_list = re.findall(re_good,str(good_list))
    for i in good_list:
        get_goods_detil(i)


    savedata(dblists)
#获取单个商品页面 商品类型编号
def get_goods_detil(id):
    #id = '100013232838'
    url = 'https://item.jd.com/'+id+'.html'
    html = httpx.get(url).text
    soup = BeautifulSoup(html,'html.parser')
    list_id = soup.find_all('div',class_= 'item')
    re_good =re.compile(r'<div class="item" data-sku="(.*?)" data-value="(.*?)">')
    for item in list_id:
        detil = re.findall(re_good,str(item))
        if len(detil) != 0:
            good_id = detil[0][0]
            dblist = get_good_detil(good_id)
            dblists.append(dblist)
        0

#获取一件物品的详细信息
def get_good_detil(id):
    url = 'https://item.jd.com/'+id+'.html#none'
    html = httpx.get(url).text
    soup = BeautifulSoup(html,'html.parser')
    title = soup.find_all(class_ ='sku-name')
    price = httpx.get('https://p.3.cn/prices/mgets?skuIds='+id).text
    price = eval(price[1:-2])['m']
    is_zy = soup.find_all(class_ = 'u-jd')
    try:
        is_zy = getmidstring(str(is_zy),r'<em class="u-jd">','</em>').strip()
    except:
        is_zy = '第三方'
    deta =r'{"mainSku":"'+id+'","version":"2","applicationEnumField":null,"addBuyBindRequest":""}'
    deta = str(deta)
    deta = str('reqData='+urllib.parse.quote(deta))
    baoxiu_list = []
    zengzhi = httpx.post('https://ms.jr.jd.com/gw/generic/bx/h5/m/queryProductIntroduce',params=deta).json()
    for i in range(0,3):
        try:
            a = zengzhi['resultData']['data']['serviceInfoList'][0]['serviceSkuDetailList'][i]
            a = a['bindSkuName'],a['price']
            baoxiu_list.append(a)
        except:
            a = ('','')
            baoxiu_list.append(a)
    try:
        name = getmidstring(str(title), r'.png">', '</img>').strip()
    except:
        name = getmidstring(str(title),r'<div class="sku-name">','</div>').strip()

    dblist = [name,is_zy,price,baoxiu_list[0],baoxiu_list[1],baoxiu_list[2]]
    print(dblist)
    return dblist


def savedata(datalist):
    book = xlwt.Workbook(encoding='utf-8',style_compression=0)
    sheet = book.add_sheet(keyword,cell_overwrite_ok=True)
    col = ("商品名称","是否自营","价格","4年全保修","5年全保修","6年全保修")
    for i in range(0,6):
        sheet.write(0,i,col[i])   #列名
    for (i,data) in zip(range(0,len(datalist)),datalist):
        for j in range(0, 6):
            if j < 3 :
                sheet.write(i + 1, j, str(data[j]))
            else:
                sheet.write(i + 1, j, str(data[j][1]))
    book.save('JD.xls')

if __name__ == '__main__':
    for i in range(1, 10):
        # 下面的print函数主要是为了方便查看当前抓到第几页了
        print('***************************************************')
        try:
            print('   First_Page:   ' + str(i))
            get_list(i)
            print('   Finish')
        except Exception as e:
            print(e)
        print('------------------')
        try:
            print('   Last_Page:   ' + str(i))
            get_list(i)
            print('   Finish')
        except Exception as e:
            print(e)
    #get_list(1)
