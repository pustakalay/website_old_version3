# Generated by Django 2.0.5 on 2018-05-20 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('translatedBy', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=2000)),
                ('publisher', models.CharField(max_length=200)),
                ('isbn', models.CharField(max_length=200)),
                ('dimension', models.CharField(max_length=200)),
                ('numberOfPages', models.CharField(max_length=200)),
                ('format', models.CharField(max_length=200)),
                ('language', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=200)),
                ('imageLocation', models.CharField(max_length=200)),
            ],
        ),
    ]
