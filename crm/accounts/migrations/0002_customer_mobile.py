# Generated by Django 3.2.7 on 2021-09-13 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='mobile',
            field=models.CharField(max_length=200, null=True),
        ),
    ]