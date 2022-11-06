# Pokescrap

A small project to retrieve information about all Pokemon from the official pokedex.

The project is configured with `poetry`, to initiate, you can do this :
```shell
poetry shell && poetry install
```

Note : ***Don't forget to configure the crawler via a .env file. (see .env.example)***

To run go to `pokemon` folder and execute spider crawling:
```shell
(venv) cd pokemon && scrapy crawl pokemon
```
