# Generated by Django 4.1.7 on 2023-03-15 04:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('sender', models.EmailField(max_length=254)),
                ('receiver', models.EmailField(max_length=254)),
                ('message', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idea', models.CharField(max_length=50)),
                ('date', models.DateField(auto_now_add=True)),
                ('desc', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Investors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=200)),
                ('document', models.FileField(upload_to='docs')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Startupfounder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=200)),
                ('document', models.FileField(upload_to='docs')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('amount', models.CharField(max_length=20)),
                ('investor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sandboxapp.investors')),
                ('statup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sandboxapp.startupfounder')),
            ],
        ),
        migrations.CreateModel(
            name='Investmentinterest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(max_length=20)),
                ('idea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sandboxapp.idea')),
                ('investor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sandboxapp.investors')),
            ],
        ),
        migrations.AddField(
            model_name='idea',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sandboxapp.startupfounder'),
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('feedback', models.CharField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sandboxapp.startupfounder')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('comment', models.CharField(max_length=200)),
                ('idea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sandboxapp.idea')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sandboxapp.startupfounder')),
            ],
        ),
    ]
