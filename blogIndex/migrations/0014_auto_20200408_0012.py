# Generated by Django 3.0.4 on 2020-04-07 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogIndex', '0013_indeximagemanagement_showonindex'),
    ]

    operations = [
        migrations.AddField(
            model_name='indeximagemanagement',
            name='ConnectArticleCateID',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='indeximagemanagement',
            name='ConnectArticleCateName',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
