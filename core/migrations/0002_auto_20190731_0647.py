# Generated by Django 2.2.3 on 2019-07-31 06:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='table',
            unique_together={('ambient', 'label')},
        ),
    ]
