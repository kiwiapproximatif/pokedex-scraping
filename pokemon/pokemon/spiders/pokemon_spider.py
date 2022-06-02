from typing import List

import scrapy

from ..items import PokemonItem
from ..settings import DEFAULT_URL, POKEMONS_NUMBER, FILE_NAME, FILE_HEADERS


class PokemonSpider(scrapy.Spider):
    name: str = 'pokemon'

    def start_requests(self):
        urls: List[str] = [f'{DEFAULT_URL}/{i}' for i in range(1, POKEMONS_NUMBER)]

        with open(FILE_NAME, 'w') as f:
            f.write(FILE_HEADERS)

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, **kwargs):
        pokemon: PokemonItem = PokemonItem()

        for container in response.css('div.container'):
            name: str = container.css('div.pokedex-pokemon-pagination-title div::text').get().strip()
            number: str = container.css('div.pokedex-pokemon-pagination-title div span::text').get().rstrip()

            for details in container.css('section.pokedex-pokemon-details'):
                types: List[str] = details.css(
                    'div.push-7 div.pokedex-pokemon-details-right div.info '
                    'div.pokedex-pokemon-attributes div.dtm-type ul li a::text'
                ).getall()
                weaknesses: List[str] = details.css(
                    'div.push-7 div.pokedex-pokemon-details-right div.info '
                    'div.pokedex-pokemon-attributes div.dtm-weaknesses ul li a span::text'
                ).getall()
                stats: List[str] = details.css(
                    'div.push-1 div.pokemon-stats-info ul li ul.gauge li.meter::attr(data-value)'
                ).getall()
                stats_name: List[str] = details.css(
                    'div.push-1 div.pokemon-stats-info ul li span::text'
                ).getall()

                pokemon['types'] = list(set([t.rstrip() for t in types]))
                pokemon['weaknesses'] = list(set([w.rstrip() for w in weaknesses]))
                pokemon['stats'] = [int(s.rstrip()) for s in stats]
                pokemon['stats_name'] = list(set([s.rstrip() for s in stats_name]))

            pokemon['name'] = name
            pokemon['number'] = number.split('.')[1]

            yield pokemon
