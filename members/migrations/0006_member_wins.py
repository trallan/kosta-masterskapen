# Generated by Django 4.2.13 on 2024-06-12 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_alter_member_hcp'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='wins',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
