# Generated by Django 4.2.13 on 2024-06-25 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0006_member_wins'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='score',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
