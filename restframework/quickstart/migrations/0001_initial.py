# Generated by Django 3.2 on 2021-04-09 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('desc', models.CharField(max_length=256, verbose_name='Description')),
                ('year', models.IntegerField(verbose_name='Publish year')),
            ],
        ),
    ]
