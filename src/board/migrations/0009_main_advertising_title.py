# Generated by Django 2.2.3 on 2019-07-31 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0008_main_advertising'),
    ]

    operations = [
        migrations.AddField(
            model_name='main_advertising',
            name='title',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]