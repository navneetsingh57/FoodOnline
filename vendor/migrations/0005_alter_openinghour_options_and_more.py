# Generated by Django 5.1.2 on 2024-10-24 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0004_openinghour'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='openinghour',
            options={'ordering': ('day', '-from_hour')},
        ),
        migrations.AlterUniqueTogether(
            name='openinghour',
            unique_together={('vendor', 'day', 'from_hour', 'to_hour')},
        ),
    ]
