# Generated by Django 3.1 on 2020-11-25 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0002_entry'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='topici',
            new_name='topic',
        ),
    ]
