#!/usr/bin/python
# -*- coding: utf-8 -*-

from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http import Request
from scrapy.spider import Rule,CrawlSpider
from scrapy.linkextractors import LinkExtractor
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor

from chen3.items import Chen3Item

class chen3Spider(CrawlSpider):
	name = "chen"
	download_delay=1
	allowed_domains=["caigou.my.gov.cn"]
	start_urls=[
		"http://caigou.my.gov.cn/ceinwz/WebInfo_List.aspx?newsid=601&jsgc=&zfcg=0100000&tdjy=&cqjy=&PubDateSort=\
		0&ShowPre=1&CbsZgys=&zbfs=&qxxx=&showqxname=0&NewsShowPre=1&wsjj=&showCgr=0&ShowOverDate=&FromUrl=sjjyxx"
		]
	rules=[
		Rule(SgmlLinkExtractor(allow=('http://caigou.my.gov.cn/ceinwz/WebInfo_List.aspx?newsid=601&jsgc=&zfcg=0100000&tdjy\
		=&cqjy=&PubDateSort=0&ShowPre=1&CbsZgys=&zbfs=&qxxx=&showqxname=0&NewsShowPre=1&wsjj=&showCgr=0&ShowOverDate\
		=&FromUrl=sjjyxx')),
		     callback='parse',
		     follow=True)
	]
	def parse(self,response):
		sel=Selector(response)
		sites=sel.xpath('//a[@id]/text()')
		items=[]
		for site in sites:
			item=Chen3Item()

			caigouname=site.extract()

			item['caigouname']=[c.encode('utf-8') for c in caigouname]
			items.append(item)
		return items
