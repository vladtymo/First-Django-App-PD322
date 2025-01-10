# Generated by Django 5.1.4 on 2025-01-10 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.IntegerField(choices=[(0, 'Admin'), (1, 'User'), (2, 'Manager')], default=0),
        ),
    ]
