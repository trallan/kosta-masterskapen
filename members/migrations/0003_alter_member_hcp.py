# Generated by Django 5.0.6 on 2024-06-11 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_member_golf_club_member_golf_id_member_hcp_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='hcp',
            field=models.CharField(max_length=4, null=True),
        ),
    ]
