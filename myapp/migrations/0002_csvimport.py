# Generated by Django 2.2.17 on 2020-12-30 17:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CsvImport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('files', models.FileField(upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['csv'])])),
            ],
        ),
    ]
