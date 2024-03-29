# Generated by Django 2.2.3 on 2019-07-31 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ambient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.IntegerField(choices=[(1, 'Solicitado'), (2, 'Preparando'), (3, 'Despachado')], default=1)),
                ('detail', models.CharField(blank=True, max_length=256, null=True)),
                ('registered_at', models.DateTimeField(auto_now_add=True)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Menu')),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=32)),
                ('active', models.BooleanField(default=True)),
                ('ambient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Ambient')),
                ('menu_set', models.ManyToManyField(related_name='table_set', through='core.Order', to='core.Menu')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='table',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Table'),
        ),
    ]
