from typing import List

import scrapy

from .pokemon import Pokemon


class PokemonSpider(scrapy.Spider):
    name: str = 'pokemon'
    FILE_NAME: str = 'pokemon.csv'
    FILE_HEADERS: str = 'name,number,types,weaknesses,stats,stats_name\n'
    DEFAULT_LANG = 'fr'
    DEFAULT_URL: str = f'https://www.pokemon.com/{DEFAULT_LANG}/pokedex'
    POKEMONS_NUMBER = 50

    def start_requests(self):
        urls: List[str] = [f'{self.DEFAULT_URL}/{i}' for i in range(1, self.POKEMONS_NUMBER)]

        with open(self.FILE_NAME, 'w') as f:
            f.write(self.FILE_HEADERS)

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, **kwargs):
        pokemon: Pokemon = Pokemon()
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

                pokemon.set_types(set([t.rstrip() for t in types]))
                pokemon.set_weaknesses(set([w.rstrip() for w in weaknesses]))
                pokemon.set_stats([int(s.rstrip()) for s in stats])
                pokemon.set_stats_name(set([s.rstrip() for s in stats_name]))

            pokemon.set_name(name)
            pokemon.set_number(number.split('.')[1])

        with open(self.FILE_NAME, 'a') as f:
            line: str = pokemon.get_csv_line()
            f.write(line)
