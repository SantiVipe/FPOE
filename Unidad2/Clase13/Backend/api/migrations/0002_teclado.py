# Generated by Django 5.0.4 on 2024-04-12 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teclado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teclado', models.CharField(blank=True, max_length=50)),
                ('swtich', models.TextField(blank=True, max_length=5000)),
                ('keycaps', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('formato', models.DateTimeField(auto_now=True, verbose_name='date updated')),
                ('conectividad', models.SlugField(blank=True, unique=True)),
            ],
        ),
    ]
