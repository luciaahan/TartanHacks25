# Generated by Django 4.2.19 on 2025-02-08 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan4me', '0002_courseinfo_fce'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalizedOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hours_study', models.CharField(max_length=20)),
                ('allocate_study', models.CharField(max_length=100)),
                ('balance', models.CharField(max_length=100)),
                ('time_prefer', models.CharField(max_length=100)),
                ('study_session', models.CharField(max_length=100)),
            ],
        ),
    ]
