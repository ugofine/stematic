# Generated by Django 3.2.5 on 2021-07-13 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('users', models.IntegerField(blank=True)),
                ('reviews', models.IntegerField(blank=True)),
                ('photo', models.ImageField(blank=True, upload_to='photo/%Y/%m/%d/')),
                ('teacher', models.CharField(max_length=20)),
                ('phototeacher', models.ImageField(blank=True, upload_to='photo/%Y/%m/%d/')),
            ],
        ),
    ]