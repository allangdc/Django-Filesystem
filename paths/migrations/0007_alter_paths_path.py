# Generated by Django 4.0.4 on 2022-05-24 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paths', '0006_alter_paths_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paths',
            name='path',
            field=models.CharField(max_length=200),
        ),
    ]