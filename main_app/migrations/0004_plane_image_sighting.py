# Generated by Django 5.1 on 2024-08-23 18:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_plane_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='plane',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.CreateModel(
            name='Sighting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.TextField(max_length=250)),
                ('registration', models.URLField(blank=True, null=True)),
                ('tracking', models.URLField(blank=True, null=True)),
                ('plane', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.plane')),
            ],
        ),
    ]
