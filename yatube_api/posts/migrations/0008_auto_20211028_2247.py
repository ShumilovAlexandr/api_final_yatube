# Generated by Django 2.2.16 on 2021-10-28 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20211028_2245'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follow',
            name='unique_pair',
        ),
    ]
