# Generated by Django 4.0.2 on 2022-02-12 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0017_rename_session_key_response_django_session_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='private_note',
            field=models.TextField(blank=True, verbose_name='Private note'),
        ),
    ]
