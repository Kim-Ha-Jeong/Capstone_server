# Generated by Django 3.0.4 on 2020-10-11 07:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Full',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_video', models.FileField(upload_to='')),
                ('date', models.DateTimeField()),
                ('size', models.CharField(max_length=20)),
                ('storage_path', models.CharField(max_length=50)),
                ('recording_time', models.TimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='full', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
