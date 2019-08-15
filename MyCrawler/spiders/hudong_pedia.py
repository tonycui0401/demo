# import scrapy
# from MyCrawler.items import HudongItem
# from scrapy.selector import Selector
# import urllib
# import re

# split_sign = '##'  # 定义分隔符


# class HudongSpider(scrapy.Spider):
#     name = "hudong"  # 爬虫启动命令：scrapy crawl hudong -o items.json -s FEED_EXPORT_ENCODING=UTF-8

#     allowed_domains = ["http://www.baike.com"]  # 声明地址域

#     #	file_object = open('merge_table3.txt','r').read()
#     file_object = open('crawled_leaf_list.txt', 'r', encoding='UTF-8').read()
#     wordList = file_object.split()  # 获取词表

#     start_urls = ['http://fenlei.baike.com']
#     count = 0

#     #	start_urls.append('http://www.baike.com/wiki/小米%5B农作物%5D')
#     #	start_urls.append('http://www.baike.com/wiki/苹果%5B果实%5D')
#     #	start_urls.append('http://www.baike.com/wiki/李%5B蔷薇科李属植物%5D')

#     # 本处是用于构造原始json
#     for i in wordList:  ##生成url列表
#         cur = "http://www.baike.com/wiki/"
#         cur = cur + str(i)
#         start_urls.append(cur)

#     #		count += 1
#     #		#print(cur)
#     #		if count > 1000:
#     #			break

#     def parse(self, response):
#         namelist = []
#         sel = Selector(response)
#         classpage = sel.xpath(
#             '//div[@class="td w-578"]/dl').extract()
#         for i in range(len(classpage)):
#             classname = re.findall(r'>.*?<', classpage[i])
#             mess = {}
#             for num in range(len(classname)):
#                 st = classname[num][1:-1]
#                 print (st)
#                 if st == "" or st == " | ":
#                     pass
#                 else:
#                     namelist.append(classname[num][1:-1])
#         for count in range(len(namelist)):
#             url = "http://fenlei.baike.com/"+ namelist[count]+"/list"
#             print (url)
#             yield scrapy.Request(url, callback=self.parse_onepage)

#     def parse_onepage(self, response):
#         soup = BeautifulSoup(response.body, "html.parser")
#         total = soup.find_all('a', href=re.compile(
#             r'http://www.baike.com/wiki/.+'))
#         for href in total:
#             try:
#                 # print href.attrs['href'][26:]
#                 # 递归爬取，不加callback试过也可以
#                 yield scrapy.Request(href.attrs['href'], callback=self.parse_w1)
#             except:
#                 continue

#     def parse_w1(self, response):
#         soup = BeautifulSoup(response.body, "html.parser")
#         # 如果不是http://www.baike.com/wiki/说明不是词条，则不作处理不保存信息
#         total = soup.find_all('a', href=re.compile(
#             r'http://www.baike.com/wiki/.+'))
#         if len(total) != 0:
#             name = {}
#             infoDict = {}
#             childinfoDict = ""

#             sel = Selector(response)
#             pagename = response.url[26:]
#             pgnametxt = re.findall(r'.*[&|?]', pagename)
#             if len(pgnametxt) != 0:
#                 pagename = pgnametxt[0][:-1]
#             pagename = urllib.unquote(pagename)
#             pgnameList = []
#             pgnameList.append(pagename)

#             sites = sel.xpath(
#                 '//div[@class="module zoom"]/table/tr/td').extract()
#             cla = sel.xpath('//div[@class="place"]/p/a/@title').extract()

#             infoDict.setdefault("infoName", ''.join(pgnameList))  # 词条名
#             infoDict.setdefault("openType", ','.join(cla))  # 开放分类
#             for site in range(len(sites)):
#                 #link = site.xpath('p/a/@title').extract()
#                 Key = re.findall(r'>.*</strong>', sites[site])
#                 Text = re.findall(r'>.*</span>', sites[site])
#                 # print Key
#                 lastTest = ""
#                 lastKey = ""
#                 test1 = ""
#                 test2 = ""
#                 if len(Key) != 0:
#                     # for num in range(len(Key)):
#                     keytxt = re.findall(r'>.*</a>', Key[0][1:-9])
#                     # print keytxt
#                     if len(keytxt) != 0:
#                         lastKey = keytxt[0][1:-5]
#                     else:
#                         lastKey = Key[0][1:-10]
#                     # print lastKey

#                 if len(Text) != 0:
#                     for num in range(len(Text)):
#                         t1 = re.findall(r'>.*?<', Text[num][:-6])
#                         for i in range(len(t1)):
#                             lastTest = lastTest + t1[i][1:-1]
#                     rtxt = re.compile(r'"')
#                     lastTest = rtxt.sub('', lastTest)
#                     # print lastTest
#                 else:  # span 中没有内容
#                     Text = re.findall(r'>.*</a>', sites[site])
#                     # print Text
#                     if len(Text) != 0:
#                         lastTest = Text[0][1:-4]
#                         # print lastTest
#                         t1 = re.findall(r'">.*', lastTest)
#                         # print t1
#                         lastTest = t1[0][2:]
#                     rtxt = re.compile(r'"')
#                     lastTest = rtxt.sub('', lastTest)
#                     # print lastTest
#                 # 先把它存成字典再作为值给键infobox
#                 #childinfoDict.setdefault(lastKey, lastTest)
#                 print (lastKey)
#                 print (lastTest)
#                 if lastKey != "" and lastKey != "":
#                     if len(sites) != 1:
#                         childinfoDict = childinfoDict + lastKey + ":" + lastTest + "@#$#"
#                     else:
#                         childinfoDict = childinfoDict + lastKey + ":" + lastTest
#             #print (childinfoDict)
#             infoDict.setdefault("infoBox", childinfoDict)  # 信息框的内容
#             yield infoDict


import scrapy
from MyCrawler.items import HudongItem
import urllib

split_sign = '##'  # 定义分隔符


class HudongSpider(scrapy.Spider):
    name = "hudong"  # 爬虫启动命令：scrapy crawl hudong -o items.json -s FEED_EXPORT_ENCODING=UTF-8

    allowed_domains = ["http://www.baike.com"]  # 声明地址域

    #   file_object = open('merge_table3.txt','r').read()
    file_object = open('crawled_leaf_list.txt', 'r', encoding='UTF-8').read()
    wordList = file_object.split()  # 获取词表

    start_urls = []
    count = 0

    #   start_urls.append('http://www.baike.com/wiki/小米%5B农作物%5D')
    #   start_urls.append('http://www.baike.com/wiki/苹果%5B果实%5D')
    #   start_urls.append('http://www.baike.com/wiki/李%5B蔷薇科李属植物%5D')

    # 本处是用于构造原始json
    for i in wordList:  ##生成url列表
        cur = "http://www.baike.com/wiki/"
        cur = cur + str(i)
        start_urls.append(cur)

    #       count += 1
    #       #print(cur)
    #       if count > 1000:
    #           break

    def parse(self, response):
        # div限定范围
        main_div = response.xpath('//div[@class="w-990"]')

        title = response.url.split('/')[-1]  # 通过截取url获取title
        title = urllib.parse.unquote(title)
        if title.find('isFrom=intoDoc') != -1:
            title = 'error'

        url = response.url  # url直接得到
        url = urllib.parse.unquote(url)

        img = ""  # 爬取图片url
        for p in main_div.xpath('.//div[@class="r w-300"]/div[@class="doc-img"]/a/img/@src'):
            img = p.extract().strip()

        openTypeList = ""  # 爬取开放域标签
        flag = 0  # flag用于分隔符处理（第一个词前面不插入分隔符）
        for p in main_div.xpath('.//div[@class="l w-640"]/div[@class="place"]/p[@id="openCatp"]/a/@title'):
            if flag == 1:
                openTypeList += split_sign
            openTypeList += p.extract().strip()
            flag = 1

        detail = ""  # 详细信息
        detail_xpath = main_div.xpath('.//div[@class="l w-640"]/div[@class="information"]/div[@class="summary"]/p')
        if len(detail_xpath) > 0:
            detail = detail_xpath.xpath('string(.)').extract()[0].strip()

        if detail == "":  # 可能没有
            detail_xpath = main_div.xpath('.//div[@class="l w-640"]/div[@id="content"]')
            if len(detail_xpath) > 0:
                detail = detail_xpath.xpath('string(.)').extract()[0].strip()

        flag = 0
        baseInfoKeyList = ""  # 基本信息的key值
        for p in main_div.xpath(
                './/div[@class="l w-640"]/div[@name="datamodule"]/div[@class="module zoom"]/table//strong/text()'):
            if flag == 1:
                baseInfoKeyList += split_sign
            baseInfoKeyList += p.extract().strip()
            flag = 1

        ## 继续调xpath！！！！！！！！！！！！！
        flag = 0
        baseInfoValueList = ""  # 基本信息的value值
        base_xpath = main_div.xpath('.//div[@class="l w-640"]/div[@name="datamodule"]/div[@class="module zoom"]/table')
        for p in base_xpath.xpath('.//span'):
            if flag == 1:
                baseInfoValueList += split_sign
            all_text = p.xpath('string(.)').extract()[0].strip()
            baseInfoValueList += all_text
            flag = 1

        item = HudongItem()
        item['title'] = title
        item['url'] = url
        item['image'] = img
        item['openTypeList'] = openTypeList
        item['detail'] = detail
        item['baseInfoKeyList'] = baseInfoKeyList
        item['baseInfoValueList'] = baseInfoValueList

        yield item

    # def parse(self, response):
    #     # div限定范围
    #     main_div = response.xpath('//div[@class="w-990"]')

    #     title = response.url.split('/')[-1]  # 通过截取url获取title
    #     title = urllib.parse.unquote(title)
    #     if title.find('isFrom=intoDoc') != -1:
    #         title = 'error'

    #     url = response.url  # url直接得到
    #     url = urllib.parse.unquote(url)

    #     img = ""  # 爬取图片url
    #     for p in main_div.xpath('.//div[@class="r w-300"]/div[@class="doc-img"]/a/img/@src'):
    #         img = p.extract().strip()

    #     openTypeList = ""  # 爬取开放域标签
    #     flag = 0  # flag用于分隔符处理（第一个词前面不插入分隔符）
    #     for p in main_div.xpath('.//div[@class="l w-640"]/div[@class="place"]/p[@id="openCatp"]/a/@title'):
    #         if flag == 1:
    #             openTypeList += split_sign
    #         openTypeList += p.extract().strip()
    #         flag = 1

    #     detail = ""  # 详细信息
    #     detail_xpath = main_div.xpath('.//div[@class="l w-640"]/div[@class="information"]/div[@class="summary"]/p')
    #     if len(detail_xpath) > 0:
    #         detail = detail_xpath.xpath('string(.)').extract()[0].strip()

    #     if detail == "":  # 可能没有
    #         detail_xpath = main_div.xpath('.//div[@class="l w-640"]/div[@id="content"]')
    #         if len(detail_xpath) > 0:
    #             detail = detail_xpath.xpath('string(.)').extract()[0].strip()

    #     flag = 0
    #     baseInfoKeyList = ""  # 基本信息的key值
    #     for p in main_div.xpath(
    #             './/div[@class="l w-640"]/div[@name="datamodule"]/div[@class="module zoom"]/table//strong/text()'):
    #         if flag == 1:
    #             baseInfoKeyList += split_sign
    #         baseInfoKeyList += p.extract().strip()
    #         flag = 1

    #     ## 继续调xpath！！！！！！！！！！！！！
    #     flag = 0
    #     baseInfoValueList = ""  # 基本信息的value值
    #     base_xpath = main_div.xpath('.//div[@class="l w-640"]/div[@name="datamodule"]/div[@class="module zoom"]/table')
    #     for p in base_xpath.xpath('.//span'):
    #         if flag == 1:
    #             baseInfoValueList += split_sign
    #         all_text = p.xpath('string(.)').extract()[0].strip()
    #         baseInfoValueList += all_text
    #         flag = 1

    #     item = HudongItem()
    #     item['title'] = title
    #     item['url'] = url
    #     item['image'] = img
    #     item['openTypeList'] = openTypeList
    #     item['detail'] = detail
    #     item['baseInfoKeyList'] = baseInfoKeyList
    #     item['baseInfoValueList'] = baseInfoValueList

    #     yield item