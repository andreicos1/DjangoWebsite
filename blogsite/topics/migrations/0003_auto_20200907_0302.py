# Generated by Django 2.2 on 2020-09-07 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0002_auto_20200906_0134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='details_html',
        ),
        migrations.AlterField(
            model_name='topic',
            name='details',
            field=models.TextField(default=' ', max_length=1024),
        ),
    ]
