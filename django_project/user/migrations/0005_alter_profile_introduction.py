# Generated by Django 4.2.4 on 2023-08-24 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_profile_introduction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='introduction',
            field=models.CharField(blank=True, default='', max_length=300),
            preserve_default=False,
        ),
    ]
