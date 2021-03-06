[![Travis](https://travis-ci.com/pjryan126/docscraper.svg?branch=master)](https://travis-ci.com/pjryan126/docscraper.svg?branch=master)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/pjryan126/docscraper.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/pjryan126/docscraper/alerts/) 
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/pjryan126/docscraper.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/pjryan126/docscraper/context:python)

# Overview

The ``docscraper`` package is a ``scrapy`` spider for crawling a given set of
websites and dowloading all available documents with a given set of file
extensions. The package is intended to be called from a Python script.

# Getting Started

You can get started by downloading the package with ``pip``:

```
$ pip install docscraper
```

Once the package is installed, you can use it with scrapy directly in your 
Python script to download files from websites as follows:

```
>>> from doccrawler import DocSpider
>>> from scrapy.crawler import CrawlerProcess
>>> allowed_domains = ["books.toscrape.com"]
>>> start_urls = ["https://books.toscrape.com"]
>>> extensions = [".html", ".pdf", ".docx", ".doc", ".svg"]
>>> process = CrawlerProcess()
>>> process.crawl(DocSpider, allowed_domains, start_urls, extensions=extensions)
>>> process.start()
```
