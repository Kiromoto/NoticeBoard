# Generated by Django 4.1.2 on 2022-10-23 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0009_response_notaccept_alter_response_accept'),
    ]

    operations = [
        migrations.RenameField(
            model_name='response',
            old_name='notaccept',
            new_name='reject',
        ),
    ]