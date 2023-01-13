from django.test import TestCase
from django.test import Client

class PageViewTests(TestCase):
    c = Client()

    def test_page_status_code(self):
        res = self.c.get('/souvenirs/')
        # res = self.c.get('/souvenirs')
        self.assertEquals(res.status_code, 200)