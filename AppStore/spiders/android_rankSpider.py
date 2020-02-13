# -*- coding: utf-8 -*-
# @Time    : 2019/6/30 17:17
# @Author  : xuzhihai0723
# @Email   : 18829040039@163.com
# @File    : rankSpider.py
# @Software: PyCharm


from scrapy import Spider, Request
from AppStore.utils import *
from AppStore.items import *
import json
from urllib.parse import urlencode
from logging import getLogger
from AppStore.login import login

class RankspiderSpider(Spider):
    name = 'android_rankSpider'
    allowed_domains = ['www.qimai.cn']
    logger = getLogger(__name__)
    url = 'https://api.qimai.cn/rank/marketRank?'
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Origin': 'https://www.qimai.cn',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36'
    }
    # 这里的参数是爬取iphone游戏畅销榜, 具体参数可根据自己需求调整
    params = {
        'market': '10',
        'category':'1',
        'country': 'cn',
        'collection': 'topselling_free',
        'date': '2020-02-10',
        # 'page': '1',
        # 'is_rank_index': '1'
    }
    cookies = login()
    cookies_, synct = get_synct()
    # cookies=cookies_

    def start_requests(self):
        self.logger.debug('正在采集第1页')
        p_str = process_params(self.params)
        analysis = get_analysis(p_str, self.synct)
        analysis="dTBxQSxacUl9cwBHdTcHTytzeBRU\
dwlHUwJmSwZwVBFuB1hdU11mXHATFxZWVg8bWwBCW1VEYlFeUyQUDlcHAFcAAgAEBwZwG1Y%3D"
        self.params.update({'analysis': analysis})
        url = self.url + urlencode(self.params)
        print(url)
        yield Request(url, headers=self.headers, cookies=self.cookies, meta={'page': 1},
                      callback=self.parse, dont_filter=True)

    def parse(self, response):
        item = QimaiItem()
        result = json.loads(response.text)
        if result['msg'] == '成功':
            max_page = result['maxPage']
            for app_info in result['rankInfo']:
                item['rank'] = app_info['index']
                item['app_id'] = app_info['appInfo']['appId']
                item['app_name'] = app_info['appInfo']['appName']
                item['country'] = app_info['appInfo']['country']
                item['icon'] = app_info['appInfo']['icon']
                item['price'] = app_info['appInfo']['price']
                item['publisher'] = app_info['appInfo']['publisher']
                item['comment_num'] = app_info['comment']['num']
                item['rating'] = app_info['comment']['rating']
                item['company_id'] = app_info['company']['id']
                item['company_name'] = app_info['company']['name']
                item['last_releasetime'] = app_info['lastReleaseTime']

                yield item

            # 下一页
            page = response.meta.get('page')
            page += 1
            if page <= max_page:
                self.logger.debug(f'正在采集第{page}页')
                del self.params['analysis']
                self.params.update({'page': str(page)})
                p_str = process_params(self.params)
                analysis = get_analysis(p_str, self.synct)
                self.params.update({'analysis': analysis})
                url = self.url + urlencode(self.params)
                yield Request(url, headers=self.headers, meta={'page': page}, cookies=self.cookies,
                              callback=self.parse, dont_filter=True)
            else:
                self.logger.debug('已采完所有页码!')
