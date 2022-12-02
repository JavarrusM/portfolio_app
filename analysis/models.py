from django.db import models

class Analysis(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    embed = models.CharField(max_length=150)
    image = models.ImageField(upload_to='analysis/images/')
    date = models.DateField()

    def __str__(self):
        return self.title

    class Meta: 
        verbose_name_plural = "analyses"
