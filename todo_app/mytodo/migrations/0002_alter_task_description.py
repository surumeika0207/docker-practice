# Generated by Django 5.0.4 on 2024-06-17 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mytodo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='詳細'),
        ),
    ]