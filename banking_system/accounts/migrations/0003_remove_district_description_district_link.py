# Generated by Django 4.1.6 on 2023-04-30 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_delete_place'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='district',
            name='description',
        ),
        migrations.AddField(
            model_name='district',
            name='link',
            field=models.CharField(default='http://localhost:8000', max_length=200),
        ),
    ]
