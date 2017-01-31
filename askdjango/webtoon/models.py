import requests
from bs4 import BeautifulSoup
from django.db import models


class Webtoon(models.Model):
    title = models.CharField(max_length=100)
    hit = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']

    @classmethod
    def crawl_naver(cls):  # cls == Webtoon
        url = "http://comic.naver.com/webtoon/weekday.nhn"
        html = requests.get(url).text
        soup = BeautifulSoup(html, 'html.parser')

        for a_tag in soup.select('.daily_all li a'):
            try:
                title = a_tag['title']
                cls.objects.create(title=title)
                print('created', title)
            except KeyError:
                pass

    # Webtoon.crawl_naver()

