# Generated by Django 4.0.3 on 2022-12-10 11:23

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_account_phonenumber'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='progress',
            name='points',
        ),
        migrations.AddField(
            model_name='progress',
            name='completion_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 10, 16, 53, 42, 331653)),
        ),
        migrations.CreateModel(
            name='Points_Assign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points_assigned', models.FloatField(blank=True, default=0.0)),
                ('intern_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interns', to=settings.AUTH_USER_MODEL)),
                ('manager_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='managers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
