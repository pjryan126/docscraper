.. docscraper documentation master file, created by
   sphinx-quickstart on Sat Mar  6 12:37:21 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

DocScraper
======================================

The ``docscraper`` package is a ``scrapy`` spider for crawling a give set of
websites and dowloading all available documents with a given set of file
extensions.

Getting Started
---------------

You can get started by downloading the package with ``pip``::

$ pip install docscraper

Once the package is installed, you can use it with scrapy directly in your
Python script to download files from websites as follows:

.. doctest::

   >>> from doccrawler import DocSpider
   >>> from scrapy.crawler import CrawlerProcess
   >>> allowed_domains = ["books.toscrape.com"]
   >>> start_urls = ["https://books.toscrape.com"]
   >>> extensions = [".html", ".pdf", ".docx", ".doc", ".svg"]
   >>> process = CrawlerProcess()
   >>> process.crawl(DocSpider, allowed_domains, start_urls, extensions=extensions)
   >>> process.start()



.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
