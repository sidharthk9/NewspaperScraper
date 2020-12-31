import scrapy
from scrapy.item import Field


class TitleItem(scrapy.Item):
    heading = Field()


class LinkItem(scrapy.Item):
    article = Field()