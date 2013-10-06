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
from tutorial import db, transmission
from scrapy.item import Item, Field

class DetailSpider(BaseSpider):
    name = "detail"
    allowed_domains = ["thepiratebay.sx"]
    #start_urls = [
            #"http://thepiratebay.sx/torrent/6808323/The_Elder_Scrolls_V_Skyrim-Razor1911",
            #]

    def __init__(self):
        items = db.get_items()
        DetailSpider.start_urls = [x.get('link') for x in items]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        items = []
        item = Detail()
        item['name'] = hxs.select('//div[@id="detailsframe"]/div[1]/text()').extract()[0]
        magnet = hxs.select('//div[@class="download"]/a[1]/@href').extract()[0]
        item['magnet'] = magnet
        items.append(item)

        transmission.magnet(magnet)
        return items

class Detail(Item):
    name = Field()
    magnet = Field()
