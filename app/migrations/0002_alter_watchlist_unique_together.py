# Generated by Django 3.2.12 on 2022-03-30 04:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='watchlist',
            unique_together={('owner', 'listing')},
        ),
    ]
