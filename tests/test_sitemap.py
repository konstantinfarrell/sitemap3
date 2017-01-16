from unittest import TestCase
from sitemap.sitemap import sitemap


class TestSiteMap(TestCase):
    def setUp(self):
        self.url = 'http://konstantinfarrell.github.io'

    def test_sitemap(self):
        results = sitemap(self.url)
        self.assertIsNotNone(results)
