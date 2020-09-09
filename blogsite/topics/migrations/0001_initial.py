# Generated by Django 3.0.3 on 2020-09-04 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('slug', models.SlugField(allow_unicode=True, unique=True)),
                ('details', models.TextField(max_length=1024)),
                ('details_html', models.TextField(blank=True, default='', editable=False)),
                ('added_date', models.DateTimeField()),
                ('image', models.ImageField(null=True, upload_to='')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]