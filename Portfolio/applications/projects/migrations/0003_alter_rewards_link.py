# Generated by Django 3.2.3 on 2021-06-08 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20210608_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rewards',
            name='link',
            field=models.URLField(blank=True, verbose_name='Link'),
        ),
    ]
