# Generated by Django 3.0.1 on 2020-03-28 23:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AdminPage', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='admin',
            options={'permissions': (('can_swap_strats', 'Can swap the strategies between two players'),)},
        ),
    ]
