from django.db import models

class Reporter(models.Model):
    #id = models.AutoField(primary_key=True, serialize=False, verbose_name='ID')
    #id = models.IntegerField(primary_key=True)
    full_name = models.CharField(max_length=70)

    def __str__(self):
        return self.full_name
