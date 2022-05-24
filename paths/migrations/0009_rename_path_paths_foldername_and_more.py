# Generated by Django 4.0.4 on 2022-05-24 21:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paths', '0008_alter_paths_parent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paths',
            old_name='path',
            new_name='foldername',
        ),
        migrations.AlterUniqueTogether(
            name='paths',
            unique_together={('foldername', 'parent')},
        ),
    ]
