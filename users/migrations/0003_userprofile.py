# Generated by Django 3.2.4 on 2021-06-25 07:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210622_1532'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.PositiveIntegerField(default=18)),
                ('tagline', models.CharField(blank=True, max_length=128)),
                ('aboutMe', models.TextField(blank=True, max_length=512)),
                ('gender', models.CharField(blank=True, choices=[('M', 'М'), ('W', 'Ж')], max_length=1)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]