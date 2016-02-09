# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import scrapy
import re
from scrapy.selector import Selector
from appstore.items import AppstoreItem

class HuaweiSpider(scrapy.Spider):
	name = "huawei"
	allowed_domains = ["huawei.com"]

	start_urls = [
		# "http://appstore.huawei.com/more/all/1",
		# "http://appstore.huawei.com/more/recommend/1",
		# "http://appstore.huawei.com/more/soft/1",
		# "http://appstore.huawei.com/more/game/1",
		# "http://appstore.huawei.com/more/newPo/1",
		# "http://appstore.huawei.com/more/newUp/1",
		 "http://appstore.huawei.com/more/all"
	] 

	def parse(self, response):
		page = Selector(response)

		hrefs = page.xpath('//h4[@class="title"]/a/@href')

		for href in hrefs:
			url = href.extract()
			yield scrapy.Request(url, callback=self.parse_item)
			# yield scrapy.Request(url, self.parse, meta={
			# 	'splash':{
			# 		'args':{'wait': 0.5},
			# 		'endpoint': 'render.html'
			# 	}
			# })

	#figure out the next page to crawl
	# def find_next_page(sefl, url):
	# 	try:
	# 		page_num_str = url.split('/')[-1]
	# 		page_num = int(page_num_str) + 1
	# 		#limit page count for testing
	# 		#if page_num > 1: crawl only specified number of pages
	# 		# return "http://google.com"
	# 		url = url[:-len(page_num_str)] + str(page_num)
	# 	except ValueError:
	# 		print "### page cannot be handled: ",
	# 		print url
	# 		return "http://google.com"

	def parse_item(self, response):
		page = Selector(response)
		item = AppstoreItem()

		item['title'] = page.xpath('//ul[@class="app-info-ul nofloat"]/li/p/span[@class="title"]/text()').extract_first().encode('utf-8')
		item['url'] = response.url
		item['appid'] = re.match(r'http://.*/(.*)', item['url']).group(1)
		item['intro'] = page.xpath('//meta[@name="description"]/@content').extract_first().encode('utf-8')

		divs = page.xpath('//div[@class="open-info"]')
		recomm = ""

		for div in divs:
			url = div.xpath('./p[@class="name"]/a/@href').extract_first()
			recommended_appid = re.match(r'http://.*/(.*)', url).group(1)
			recommended_appname = div.xpath('./p[@class="name"]/a/text()').extract_first().encode('utf-8')
			recomm += "{0}:{1},".format(recommended_appid, recommended_appname)

		item['recommended'] = recomm
		yield item


