# Generated by Django 4.0.5 on 2022-06-23 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grid', '0002_alter_visit_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='employers'),
        ),
    ]
