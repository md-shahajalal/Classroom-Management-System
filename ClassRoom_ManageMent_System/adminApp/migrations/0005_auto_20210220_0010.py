# Generated by Django 2.2.3 on 2021-02-19 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminApp', '0004_auto_20210219_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='notice_timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
