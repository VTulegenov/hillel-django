# Generated by Django 4.1.6 on 2023-03-23 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0015_bookannotation'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='starred',
            field=models.BooleanField(default=False),
        ),
    ]
