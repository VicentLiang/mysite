from django.forms import ModelForm, Textarea
from news.models.article import Article

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['pub_date', 'headline', 'content', 'reporter']
        widgets = {
            'content': Textarea(attrs={'cols': 80, 'rows': 20}),
        }
