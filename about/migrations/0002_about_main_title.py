# Generated by Django 3.2 on 2021-05-11 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='main_title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
