# Generated by Django 4.0.4 on 2022-05-10 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_politicalparty_alter_candidate_party'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='candidate_picture',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]