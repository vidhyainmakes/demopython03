# Generated by Django 4.1.6 on 2023-05-04 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_district_description_district_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbankaccount',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='Female', max_length=1),
        ),
    ]
