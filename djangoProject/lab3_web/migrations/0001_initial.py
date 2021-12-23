# Generated by Django 3.2.8 on 2021-11-23 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='lab3_web/static/images', verbose_name='images')),
                ('title', models.CharField(max_length=50, verbose_name='Flowers')),
                ('price', models.CharField(max_length=250, verbose_name='Price')),
            ],
        ),
    ]
