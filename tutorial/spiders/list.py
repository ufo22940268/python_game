#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2013 ccheng <ccheng@cchengs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.

"""

"""
from scrapy.spider import BaseSpider
from scrapy.selector import *
from tutorial import db
from scrapy.item import Item, Field

class ListSpider(BaseSpider):
    name = "list"
    allowed_domains = ["thepiratebay.sx"]
    start_urls = [
            "http://thepiratebay.sx/top/400",
            ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        items = []
        dets = hxs.select('//div[@class="detName"]')
        links = []
        for det in dets:
            item = Website()
            item['name'] = det.select('a/text()').extract()
            link = 'http://thepiratebay.sx' + det.select('a/@href').extract()[0]
            links.append(link)
            item['link'] = link
            items.append(item)

        #Clear database first.
        #db.clear_game()

        for item in items: 
            db.insert_item(dict(item))
        return items

class Website(Item):
    link = Field()
    name = Field()

