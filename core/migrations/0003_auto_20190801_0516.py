# Generated by Django 2.2.3 on 2019-08-01 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190731_0647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ambient',
            name='name',
            field=models.CharField(max_length=128, unique=True),
        ),
    ]
