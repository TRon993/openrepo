# Generated by Django 4.0.7 on 2022-11-15 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repo', '0002_default_superuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='repository',
            name='architecture',
        ),
        migrations.AddField(
            model_name='package',
            name='architecture',
            field=models.CharField(db_index=True, default='', max_length=256),
            preserve_default=False,
        ),
    ]
