# Generated by Django 4.2.1 on 2023-11-23 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sandboxapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkSpace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100)),
                ('size', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='land_images/')),
                ('status', models.CharField(default='Free', max_length=100)),
            ],
        ),
    ]
