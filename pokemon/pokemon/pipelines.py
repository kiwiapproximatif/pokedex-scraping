# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class PokemonPipeline:
    FILE_NAME: str = 'pokemon.csv'

    def process_item(self, item, spider):
        with open(self.FILE_NAME, 'a') as f:
            line: str = f"{item['name']},{item['number']},{item['types']},{item['weaknesses']},{item['stats']},{item['stats_name']}\n"
            f.write(line)

        return item
