# Generated by Django 3.0.4 on 2020-04-05 18:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('blogIndex', '0009_auto_20200406_0155'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndexImageManagement',
            fields=[
                ('IndexImageID', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('IndexImageName', models.CharField(max_length=100)),
                ('IndexImageUrl', models.CharField(max_length=200)),
                ('CreateTime', models.DateTimeField(auto_now_add=True)),
                ('ConnectArticleID', models.CharField(max_length=100)),
                ('ConnectArticleName', models.CharField(max_length=100)),
                ('UpdateTime', models.DateTimeField(auto_now=True)),
                ('IsDeleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.RenameField(
            model_name='indeximage',
            old_name='IndexImage',
            new_name='Image',
        ),
        migrations.RenameField(
            model_name='indeximage',
            old_name='IndexImageID',
            new_name='ImageID',
        ),
        migrations.RemoveField(
            model_name='indeximage',
            name='ConnectArticleID',
        ),
        migrations.RemoveField(
            model_name='indeximage',
            name='ConnectArticleName',
        ),
    ]
