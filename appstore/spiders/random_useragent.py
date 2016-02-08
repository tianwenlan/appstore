# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import random

from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware


class RandomUserAgentMiddleware(UserAgentMiddleware):
	def __int__(self, settings, user_agent='Scrapy'):
		super(RandomUserAgentMiddleware, self).__init__()
		self.user_agent = user_agent

	def process_request(self, request, spider):
		ua = random.choice(self.user_agent)
		#ua = "Scrapy/VERSION (+http://scrapy.org)"
		print "**********Current UserAgent:%s**************" %ua
		request.headers.setdefault('User-Agent', ua)

		#the default user_agent_list composes chrome, IE, firefox, Mozilla, opera, netscape
		#for more user agent strings, you can find it in http://www.useragentstring.com/pages/useragentstring.php

		user_agent_list = [
			"Mozilla/5.0 (Windowns NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
			"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:43.0) Gecko/20100101 Firefox/43.0",
		]





