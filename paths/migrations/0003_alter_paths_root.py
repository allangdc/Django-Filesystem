# Generated by Django 4.0.4 on 2022-05-23 00:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('paths', '0002_paths_root'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paths',
            name='root',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='paths.paths'),
        ),
    ]