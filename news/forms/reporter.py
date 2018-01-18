from django.forms import ModelForm, Textarea
from news.models.reporter import Reporter

class ReporterForm(ModelForm):
    class Meta:
        model = Reporter
        fields = '__all__'
