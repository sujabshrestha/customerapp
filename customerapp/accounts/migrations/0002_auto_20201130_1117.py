# Generated by Django 3.1.3 on 2020-11-30 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(default='', max_length=200),
        ),
    ]
