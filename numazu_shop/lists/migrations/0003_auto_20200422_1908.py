# Generated by Django 3.0.5 on 2020-04-22 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0002_article_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='text',
            field=models.TextField(max_length=512),
        ),
        migrations.AlterField(
            model_name='shop',
            name='desc',
            field=models.TextField(max_length=512),
        ),
        migrations.AlterField(
            model_name='shop',
            name='link',
            field=models.TextField(max_length=512),
        ),
    ]
