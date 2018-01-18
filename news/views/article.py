from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from news.models.reporter import Reporter
from news.models.article import Article
from news.forms.reporter import ReporterForm
from news.forms.article import ArticleForm

# Create your views here.
def year_archive(request, year):
    a_list = Article.objects.filter(pub_date__year=year)
    context = {'year': year, 'article_list': a_list}
    return render(request, 'news/year_archive.html', context)

def article(request):
    list = Article.objects.all()
    context = {'list': list}
    return render(request, 'news/archive_list.html', context)

def add(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        form.save()
        return HttpResponseRedirect('/news/article/')
    else:
        form = ArticleForm()
        return render(request, 'news/archive_save.html', {'form': form})

def change(request, id):
    article = get_object_or_404(Article, pk = id)
    if request.method == 'GET':
        form = ArticleForm(instance=article)
        form.id = id
        return render(request, 'news/archive_save.html', {'form': form})
    else:
        form = ArticleForm(request.POST, instance=article)
        form.save()
        return HttpResponseRedirect('/news/article/')

def delete(request, id):
    article = Article.objects.get(id = id)
    article.delete()
    return HttpResponseRedirect('/news/article/')
