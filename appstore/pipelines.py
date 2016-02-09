# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy import signals
import json
import pymongo

class AppstorePipeline(object):
 	def __init__(self):
		self.file = open('appstore.dat', 'wb')
	
	def process_item(self, item, spider):
		val = "{0}\t{1}\t{2}\n".format(item['appid'], item['title'], item['intro'])
		self.file.write(val)
		return item

class JsonWriterPipeline(object):
	def __init__(self):
		self.file = open('appstore.json', 'wb')
		
	# def open_spider(self, spider):
	# 	self.file.write('{\n\t"appstore":[\n')

	def process_item(self, item, spider):
		line = json.dumps(dict(item), ensure_ascii=False) + "\n"
		self.file.write(line)
		return item

	# def close_spider(self, spider):
	# 	self.file.write('\t]\n}')
	# 	self.file.close()

# class MongoPipeline(object):
#     collection_name = 'scrapy_items'
#     def __init__(self, mongo_uri, mongo_db):
#         self.mongo_uri = mongo_uri
#         self.mongo_db = mongo_db

#     @classmethod
#     def from_crawler(cls, crawler):
#         return cls(
#             mongo_uri=crawler.settings.get('MONGO_URI'),
#             mongo_db=crawler.settings.get('MONGO_DATABASE', 'items')
#         )

#     def open_spider(self, spider):
#         self.client = pymongo.MongoClient(self.mongo_uri)
#         self.db = self.client[self.mongo_db]

#     def close_spider(self, spider):
#         self.client.close()

#     def process_item(self, item, spider):
#         self.db[self.collection_name].insert(dict(item))
#         return item
