# Generated by Django 3.2.4 on 2021-06-22 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_blog_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(default='', max_length=20),
        ),
    ]
