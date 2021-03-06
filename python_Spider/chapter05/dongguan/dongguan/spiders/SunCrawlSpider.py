#-*- coding:utf-8 -*-

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule, CrawlSpider
from dongguan.items import DongguanItem
import time

class SunCrawlSpider(CrawlSpider):
	name = "suncrawl"
	allowed_domains = ['wz.sun0769.com']
	start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=']

	#每一页的匹配规则
	pagelink = LinkExtractor(allow=('type=4'))
	#每个帖子的匹配规则
	contentlink = LinkExtractor(allow = (r'/html/question/\d+/\d+.shtml'))
	rules = [
		#本例为特殊情况，需要调用deal_links方法处理每个页面里的链接
		# Rule(pagelink, process_links = "deal_links", follow=True),
		Rule(pagelink, follow=True),
		Rule(contentlink, callback = 'parse_item')
	]

	#需要重新处理每个页面里的链接，将链接里的'Type&type=4?page=xxx'替换为'Type?type=4&page=xxxx'(或者是Type&page=xxx?type=4替换为'Type?page=xxx&type=4')否则无法发送这个链接

	def parse_item(self, response):
		print("url:%s"%response.url)
		item = DongguanItem()
		# 标题
		item['title'] = response.xpath('//head/title/text()').extract()[0].replace('_阳光热线问政平台', "")
		#编号
		item['number'] = (response.xpath('//div[@class="pagecenter p3"]//strong//text()').extract()[0]).split(':')[-1]

		#帖子内容,默认取出有图片情况下的文字内容列表
		content = response.xpath('//div[@class="contentext"]/text()').extract()
		#如果没有图片，则取出没有图片情况下的文字内容列表
		if len(content) == 0:
			content = response.xpath('//div[@class="c1 text14_2"]/text()').extract()
		
		item['content'] = "".join(content).strip()

		#链接
		item['url'] = response.url
		#帖子状态
		item['status'] =  response.xpath('//div[@class="audit"]//span/text()').extract()[0]

		#网友
		item['net_friend'] = (response.xpath('//div[@class="cright"]//p//text()').extract()[0]).split("发言时间")[0].split("：")[1].strip()
		#时间
		item['time'] = (response.xpath('//div[@class="cright"]//p//text()').extract()[0]).split("发言时间")[1].strip()
		# yield item
		yield item

