# Generated by Django 2.1.7 on 2019-02-21 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_accounts', '0003_auto_20190221_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='category',
            field=models.CharField(choices=[('Individual', 'Individual'), ('Company', 'Company')], default='Individual', max_length=100),
        ),
    ]