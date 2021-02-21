# -*- coding: utf-8 -*-

# Scrapy settings for newspy
#

BOT_NAME = 'newspy'

SPIDER_MODULES = ['newspy.spiders']
NEWSPIDER_MODULE = 'newspy.spiders'


# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

#COOKIES_ENABLED = False

#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

#SPIDER_MIDDLEWARES = {
#    'newspy.middlewares.NewspySpiderMiddleware': 543,
#}

#DOWNLOADER_MIDDLEWARES = {
#    'newspy.middlewares.MyCustomDownloaderMiddleware': 543,
#}

#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

ITEM_PIPELINES = {
    'newspy.pipelines.MongoDBPipeline': 100
}

#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

DEPTH_LIMIT = 3
DOWNLOAD_DELAY = 2

MONGODB_HOST = 'aws-eu-west-1-portal.8.dblayer.com'
MONGODB_PORT = 17162
MONGODB_USER = 'newspy'
MONGODB_PASS = 'e6h65J6I4vilmjS'
MONGODB_DB = 'scrapy'
MONGODB_COLLECTION = 'news'
