# Generated by Django 4.0.4 on 2022-05-24 05:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paths', '0005_paths_parent'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='paths',
            unique_together={('path', 'parent')},
        ),
    ]
