# Generated by Django 3.0.4 on 2020-04-04 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0004_auto_20200401_1358'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='IsSuperUseer',
            field=models.BooleanField(default=False),
        ),
    ]
