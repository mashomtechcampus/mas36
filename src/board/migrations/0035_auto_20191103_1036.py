# Generated by Django 2.2.3 on 2019-11-03 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0034_auto_20191103_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='description',
            field=models.TextField(default='لايوجد وصف', max_length=500),
        ),
    ]
