# Generated by Django 2.2.3 on 2019-08-01 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20190801_0516'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='registered_at',
            new_name='requested_at',
        ),
        migrations.AddField(
            model_name='order',
            name='dispatched_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]