# -*- coding: utf-8 -*-
import scrapy
from scraping.items import GoogleNewsDetailItem
from scrapy_splash import SplashRequest
import logging

class GoogleNewsFreelanceSpider(scrapy.Spider):
    name = 'google_news_freelance'
    allowed_domains = ['www.google.co.jp']
    start_urls = ['https://www.google.co.jp/search?hl=ja&source=lnms&tbm=nws&sa=X&q=フリーランス']
    logging.basicConfig(filename='example.log',level=logging.DEBUG)

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, args={'wait': 3})

    def parse(self, response):
        #--------------------------------------------------
        PAGE_LOOP_MAX = 10
        #--------------------------------------------------
        page_loop_num = 0
        #--------------------------------------------------
        logging.debug("----------------------------")
        logging.debug("html body:")
        logging.debug(str(response.body))
        logging.debug("----------------------------")
        for topic in response.css('.g'):
            item = GoogleNewsDetailItem()
            item['headline'] = topic.css('a::text').extract_first()
            item['url'] = topic.css('a::attr(href)').extract_first()
            yield item

        #next_page = response.xpath('//*[@id="pnnext"]').css('a::attr(href)').extract_first()
        next_page = response.xpath('//*[@id="pnnext"]')
        logging.debug("----------------------------")
        logging.debug("next_page:" + str(next_page))
        logging.debug("----------------------------")
        #最大ループ回数制限
        if page_loop_num > PAGE_LOOP_MAX :
            next_page = None

        if next_page is not None:
            page_loop_num += 1
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback = self.parse)
