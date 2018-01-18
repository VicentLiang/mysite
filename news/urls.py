from django.urls import path, re_path

from news.views import article
from news.views import reporter

urlpatterns = [
    path('articles/<int:year>/', article.year_archive),
    #path('articles/<int:year>/<int:month>/', views.month_archive),
    #path('articles/<int:year>/<int:month>/<int:pk>/', views.article_detail),
    path('article/', article.article),
    path('article/<int:id>/change/', article.change, name='article_change'),
    path('article/add/', article.add, name='article_add'),
    path('article/<int:id>/delete/', article.delete, name='article_delete'),

    path('reporter/', reporter.reporter),
    path('reporter/<int:id>/change/', reporter.change, name='reporter_change'),
    #re_path(r'reporters/to_save/\d*/?$', views.to_save_reporter),
    path('reporter/add/', reporter.add, name='reporter_add'),
    path('reporter/<int:id>/delete/', reporter.delete, name='reporter_delete'),

]
