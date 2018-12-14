import requests,random,time
from bs4 import BeautifulSoup as bs


url="https://yingyang.51240.com/"       #便民查询网


allhead=['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
         'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60',
         'Opera/8.0 (Windows NT 5.1; U; en)',
        'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
        'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',
         'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko']

def get_sort(urin):      #获取所有分类，以及分类的链接，做成字典
    aa = requests.get(urin, headers={'user-agent': random.choice(allhead)})
    bb = bs(aa.content, 'lxml')
    cc=bb.find(class_='xiaoshuomingkuang_neirong')
    dd=cc.find_all('p')
    ff=dd[1].find_all('a')
    out={}
    for i in ff:
        out[i.text]=url+i.get('href')[1:]
    return out

def get_content(sort,urin):     #获取某一分类的所有食物，以及食物链接，做出字典
    aa = requests.get(urin, headers={'user-agent': random.choice(allhead)})
    bb = bs(aa.content, 'lxml')
    cc=bb.find(class_='list')
    dd=cc.find_all('li')
    out={}
    for i in dd:
        out[i.text]=url+i.find('a').get('href')[1:]
    return out

def get_ele(con,urin):      #获取某一食物的所有营养成分，对应数量以及单位，做出字典
    aa = requests.get(urin, headers={'user-agent': random.choice(allhead)})
    bb = bs(aa.content, 'lxml')
    cc = bb.find(class_='yingyang wkbx')
    dd=cc.find_all('tr')
    out={}
    def v_u(str1):
        str1=str1.replace('(','')
        str1 = str1.replace(')', '')
        val=float(str1.split(' ')[0])
        unit=str1.split(' ')[1]
        return [val,unit]
    for i in dd:
        te=i.text
        dat = te.split('\n')
        out[dat[1]] = v_u(dat[2])
        out[dat[3]] = v_u(dat[4])
    return out



if __name__=="__main__":
    all_sort=get_sort(url)
    a1=get_content('谷类',all_sort['谷类'])
    get_ele('小麦',a1['小麦'])
