# Generated by Django 4.0.4 on 2022-04-20 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_remove_event_candidate_event_candidate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='candidate',
            field=models.ManyToManyField(related_name='events', to='polls.candidate'),
        ),
    ]
