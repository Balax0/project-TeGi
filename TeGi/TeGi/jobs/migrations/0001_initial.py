# Generated by Django 5.1.4 on 2025-01-04 15:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('job_type', models.CharField(choices=[('Freelancer', 'Freelancer'), ('Part Time', 'Part Time'), ('Full Time', 'Full Time'), ('Work From Home', 'Work From Home'), ('Onfield', 'Onfield')], max_length=50)),
                ('location', models.CharField(max_length=100)),
                ('timing', models.CharField(max_length=50)),
                ('pay_range', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('experience_required', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_gig', models.BooleanField(default=False)),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skills', models.TextField()),
                ('description', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=15)),
                ('age', models.IntegerField()),
                ('experience', models.TextField()),
                ('talents', models.TextField()),
                ('resume', models.FileField(upload_to='resumes/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
