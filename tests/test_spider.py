import os
import shutil
from unittest import main

from docscraper.spider import DocLinkExtractor, crawl
import pandas as pd

from .base import BaseTestCase


class TestDocLinkExtractor(BaseTestCase):

    def setUp(self):
        super(self.__class__, self).setUp()
        self.extractor = DocLinkExtractor(self.EXTENSIONS)

    def tearDown(self):
        super(self.__class__, self).tearDown()
        self.extractor = None

    def test_deny_extensions(self):
        for ext in self.EXTENSIONS:
            self.assertNotIn(ext, self.extractor.deny_extensions)


class TestDocSpider(BaseTestCase):

    @classmethod
    def setUpClass(cls):
        """ Run crawl only once for all test cases in the class. """
        super(TestDocSpider, cls).setUpClass()
        crawl(cls.ALLOWED_DOMAINS,
              cls.START_URLS,
              directory=cls.DIRECTORY,
              extensions=cls.EXTENSIONS)

    @classmethod
    def tearDownClass(cls):
        super(TestDocSpider, cls).tearDownClass()
        shutil.rmtree(cls.DIRECTORY)

    def test_document_directories_created(self):
        for domain in self.ALLOWED_DOMAINS:
            directory = os.path.join(self.DIRECTORY, domain)
            self.assertTrue(os.path.exists(directory))

    def test_documents_downloaded(self):
        for domain in self.ALLOWED_DOMAINS:
            directory = os.path.join(self.DIRECTORY, domain)
            self.assertTrue(len(os.listdir(directory)) > 0)

    def test_file_listing(self):
        df = pd.read_excel(f"{self.DIRECTORY}/file-listing.xlsx")
        count = sum([len(files) for r, d, files in os.walk(self.DIRECTORY)])
        # file-listing is included in count
        self.assertTrue(df.shape[0] == count - 1)


if __name__ == "__main__":
    main()

