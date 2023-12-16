from django.db import models
#django orm - прочесть дома
# Create your models here.

class Students(models.Model):
    name=models.CharField(max_length=255, verbose_name='имя')
    nomer=models.CharField(max_length=255, verbose_name='номер')
    avatarka = models.ImageField()

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name='Студенты'