# Generated by Django 4.0.4 on 2022-05-24 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('paths', '0007_alter_paths_path'),
        ('files', '0005_files_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='path',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='paths.paths'),
        ),
    ]
