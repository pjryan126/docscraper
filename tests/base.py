import os
import shutil
from unittest import main, TestCase


class BaseTestCase(TestCase):

    NAME = "Test Spider"
    ALLOWED_DOMAINS = ["books.toscrape.com"]
    START_URLS = ["https://books.toscrape.com"]
    DIRECTORY = os.path.abspath("./tests/output")
    EXTENSIONS = [".html", ".pdf", ".docx", ".doc", ".svg"]
