from unittest import TestCase
from sitemap.sitemap import sitemap


class TestSiteMap(TestCase):
    def setUp(self):
        self.url = 'http://konstantinfarrell.github.io'
        self.bigger_site = 'https://learnxinyminutes.com'

    def test_sitemap(self):
        results = sitemap(self.url, write=False)
        self.assertIsNotNone(results)

    def test_bigger_sitemap(self):
        results = sitemap(self.bigger_site, write=False)
        self.assertIsNotNone(results)
