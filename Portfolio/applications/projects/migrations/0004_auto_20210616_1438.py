# Generated by Django 3.2.3 on 2021-06-16 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_alter_rewards_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='languages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='nombre')),
                ('typed', models.BooleanField(verbose_name='Tipado')),
            ],
            options={
                'verbose_name': 'Lenguaje',
                'verbose_name_plural': 'Lenguajes',
            },
        ),
        migrations.AddField(
            model_name='projects',
            name='languages',
            field=models.ManyToManyField(to='projects.languages'),
        ),
    ]