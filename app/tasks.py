from __future__ import absolute_import, unicode_literals
from .models import Url as U
import urllib.request
from celery import shared_task

@shared_task
def tiny_url(url, pk):
    apiurl = "https://clck.ru/--?url="
    tinyurl = urllib.request.urlopen(apiurl + url).read()
    x = U.objects.get(pk=pk)
    x.short_url = tinyurl.decode("utf-8")
    x.save()
    return True