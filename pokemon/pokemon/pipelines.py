# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

from .settings import FILE_NAME, DEFAULT_LANG


class PokemonPipeline:
    def process_item(self, item, spider):
        with open(f'{FILE_NAME}_{DEFAULT_LANG}.csv', 'a') as f:
            line: str = f"{item['name']},{item['number']},{item['types']},{item['weaknesses']},{item['stats']},{item['stats_name']}\n"
            f.write(line)

        return item
