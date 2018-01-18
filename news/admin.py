from django.contrib import admin
from news.models import article
from news.models import reporter
# Register your models here.
admin.site.register(article.Article)
admin.site.register(reporter.Reporter)
