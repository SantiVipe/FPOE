# Generated by Django 5.0.4 on 2024-04-12 02:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_teclado'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teclado',
            old_name='swtich',
            new_name='switch',
        ),
    ]
