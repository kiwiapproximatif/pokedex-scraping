# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

from .settings import FILE_NAME, DEFAULT_LANG, BATCH_SIZE


class PokemonPipeline(object):
    def __init__(self):
        super(PokemonPipeline, self).__init__()
        self.items = []

    def add_item(self, item):
        self.items.append(
            f"{item['name']},{item['number']},{item['types']},{item['weaknesses']},{item['stats']},{item['stats_name']}\n"
        )

    def write_items(self):
        with open(f'{FILE_NAME}_{DEFAULT_LANG}.csv', 'a') as f:
            f.writelines(self.items)

        self.items.clear()

    def process_item(self, item, spider):
        self.add_item(item)

        if len(self.items) >= BATCH_SIZE:
            self.write_items()

        return item

    def close_spider(self, spider):
        self.write_items()
