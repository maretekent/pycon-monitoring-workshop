# Generated by Django 2.1.2 on 2018-10-13 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='messagerequest',
            old_name='messagePayload',
            new_name='data',
        ),
    ]