# Generated by Django 4.0.4 on 2022-04-27 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_alter_event_deadline'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='deadline',
            new_name='date',
        ),
    ]