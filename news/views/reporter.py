from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from news.models.reporter import *
from news.forms.reporter import *

# Create your views here.

def reporter(request):
    list = Reporter.objects.all()
    context = {'list': list}
    return render(request, 'news/reporter_list.html', context)

def change(request, id):
    reporter = get_object_or_404(Reporter,pk = id)
    if request.method == 'POST':
        form = ReporterForm(request.POST,instance=reporter)
        form.save()
        return HttpResponseRedirect('/news/reporter/')
    else:
        form = ReporterForm(instance=reporter)
        form.id = id
        return render(request, 'news/reporter_save.html', {'form': form})

def add(request):
    if request.method == 'POST':
        print('Post', request.POST)
        form = ReporterForm(request.POST)
        form.save()
        return HttpResponseRedirect('/news/reporter/')
    else:
        form = ReporterForm()
        return render(request, 'news/reporter_save.html', {'form': form})


def delete(request, id):
    Reporter.objects.filter(id = id).delete()
    return HttpResponseRedirect('/news/reporter/')
