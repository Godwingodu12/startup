# Generated by Django 4.2.1 on 2023-11-24 04:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sandboxapp', '0003_alter_workspace_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='workspace',
            name='sfid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sandboxapp.startupfounder'),
        ),
        migrations.AlterField(
            model_name='workspace',
            name='image',
            field=models.FileField(upload_to='land_images'),
        ),
    ]