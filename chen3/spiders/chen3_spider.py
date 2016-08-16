#!/usr/bin/python
# -*- coding: utf-8 -*-

from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy import log

from chen3.items import Chen3Item

class chen3Spider(Spider):
	name = "chen"
	allowed_domains=["caigou.my.gov.cn"]
	start_urls=[
		"http://caigou.my.gov.cn/ceinwz/WebInfo_List.aspx?newsid=601&jsgc=&zfcg=0100000&tdjy=&cqjy=&PubDateSort=\
		0&ShowPre=1&CbsZgys=&zbfs=&qxxx=&showqxname=0&NewsShowPre=1&wsjj=&showCgr=0&ShowOverDate=&FromUrl=sjjyxx"
	]
def parse(self,response):
	sel=Selector(response)
	for i in range(2,101):
		xpaths="/html/body/form/div[3]/span/table[2]/tbody/tr/td/table[3]/tbody/tr/td[2]/table/tbody/tr[2]/td/table/\
		tbody/tr/td/div/table/tbody/tr("+"str(i)"+")/td[2]/a"
		sites=sel.xpath(xpaths)
		items=[]
		for site in sites:
			item=Chen3Item()

			caigouname=site.extract()

			item['caigouname']=[c.encode('utf-8') for c in caigouname]
			items.append(item)

			log.msg("Appending item...",level='INFO')

		log.msg("Appending done",level="INFO")
		return items
