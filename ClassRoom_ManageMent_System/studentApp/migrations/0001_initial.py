# Generated by Django 2.2.3 on 2021-02-19 15:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TeachingClass',
            fields=[
                ('teaching_class_id', models.AutoField(primary_key=True, serialize=False)),
                ('teaching_class_slug', models.SlugField(blank=True, max_length=250, null=True)),
                ('teaching_class_name', models.TextField(max_length=200)),
                ('teaching_class_subject', models.TextField(max_length=70)),
                ('teaching_class_section', models.TextField(max_length=5)),
                ('teaching_class_timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('teaching_class_class_code', models.CharField(max_length=20)),
                ('teaching_class_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
