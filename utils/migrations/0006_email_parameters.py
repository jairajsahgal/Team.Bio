# Generated by Django 4.2.5 on 2023-09-25 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0005_gptmodel_primary'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='parameters',
            field=models.TextField(blank=True, null=True),
        ),
    ]
