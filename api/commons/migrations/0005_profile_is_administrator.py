# Generated by Django 3.2 on 2021-06-15 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commons', '0004_alter_group_mnemonic'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_administrator',
            field=models.BooleanField(default=False),
        ),
    ]
