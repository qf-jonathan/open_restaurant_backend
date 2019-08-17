# Generated by Django 2.2.3 on 2019-08-03 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20190802_0518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='core.Menu'),
        ),
        migrations.AlterField(
            model_name='order',
            name='table',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='core.Table'),
        ),
    ]
