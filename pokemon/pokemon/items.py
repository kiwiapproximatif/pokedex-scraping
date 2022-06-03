# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
from typing import List

import scrapy


class PokemonItem(scrapy.Item):
    name: str = scrapy.Field()
    number: str = scrapy.Field()
    types: List[str] = scrapy.Field()
    weaknesses: List[str] = scrapy.Field()
    stats: List[int] = scrapy.Field()
    stats_name: List[str] = scrapy.Field()
