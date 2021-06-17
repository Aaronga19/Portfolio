# Generated by Django 3.2.3 on 2021-06-17 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20210616_1438'),
    ]

    operations = [
        migrations.CreateModel(
            name='framework',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='nombre')),
            ],
            options={
                'verbose_name': 'Framework',
                'verbose_name_plural': 'Frameworks',
            },
        ),
        migrations.AddField(
            model_name='projects',
            name='frameworks',
            field=models.ManyToManyField(to='projects.framework'),
        ),
    ]
