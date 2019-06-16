# Generated by Django 2.1.7 on 2019-02-20 19:54

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='blog_posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Initiative_Title', models.CharField(max_length=255, unique=True)),
                ('requirements', models.CharField(default=' ', max_length=40000)),
                ('name', models.CharField(max_length=100)),
                ('budget', models.PositiveIntegerField(default=0)),
                ('location', models.CharField(default='', max_length=100)),
                ('num_of_attendees', models.PositiveIntegerField(blank=True, default=0)),
                ('attendees', models.ManyToManyField(blank=True, related_name='attending', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
