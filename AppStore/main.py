from scrapy.cmdline import execute

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# execute(["scrapy", "crawl", "rankSpider","-o","jsondata/appstore_cn_2.10.json"])
execute(["scrapy", "crawl", "android_rankSpider","-o","jsondata/google_cn_2.10.json"])