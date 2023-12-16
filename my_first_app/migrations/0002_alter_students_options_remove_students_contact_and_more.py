# Generated by Django 4.1.7 on 2023-09-16 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_first_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='students',
            options={'verbose_name': 'Студенты'},
        ),
        migrations.RemoveField(
            model_name='students',
            name='contact',
        ),
        migrations.AddField(
            model_name='students',
            name='nomer',
            field=models.CharField(default=1, max_length=255, verbose_name='номер'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='students',
            name='name',
            field=models.CharField(max_length=255, verbose_name='имя'),
        ),
    ]
