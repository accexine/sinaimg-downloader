#coding=utf-8
from urllib import urlopen
from re import compile
img_finder = compile('/(?:middle|orignal|small)/(\w{21})"')
def downimg(id):
    return urlopen('http://s4.sinaimg.cn/orignal/'+id).read()

def blog(url):
    '''返回博客页面中的所有图像的二进制数据。'''
    return [downimg(i) for i in img_finder.findall(urlopen(url).read())]

def category(url):
    '''返回相册内所有图像的二进制数据。'''
    page,imgs = 1,[]
    while True:
        web = urlopen(url+'/page'+page).read()
        [imgs.append(downimg(i)) for i in img_finder.findall(web)]
        if '下一页' in web:
            page += 1
        else:
            return imgs
