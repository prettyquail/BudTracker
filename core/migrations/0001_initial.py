# Generated by Django 4.0.3 on 2022-03-12 23:34

import core.models
from django.conf import settings
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('user_type', models.CharField(choices=[('MANAGER', 'manager'), ('INTERN', 'intern')], default='INTERN', max_length=50, verbose_name='Type')),
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, unique=True, validators=[django.core.validators.EmailValidator()])),
                ('username', models.CharField(max_length=66, unique=True)),
                ('profile_image', models.ImageField(blank=True, default=core.models.get_default_profile_image, max_length=255, null=True, upload_to=core.models.get_profile_image_filepath)),
                ('phoneNumber', models.CharField(max_length=16, unique=True, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{8,15}$')])),
                ('date_joined', models.DateField(auto_now_add=True, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Blocker',
            fields=[
                ('blocker_id', models.AutoField(primary_key=True, serialize=False)),
                ('label', models.CharField(max_length=66)),
                ('query', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('task_id', models.AutoField(primary_key=True, serialize=False)),
                ('deadline', models.DateTimeField()),
                ('task_name', models.CharField(max_length=66)),
                ('description', models.TextField(blank=True, null=True)),
                ('status', models.DecimalField(decimal_places=0, default=0, max_digits=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('completed', models.BooleanField(default=False)),
                ('intern_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='intid', to=settings.AUTH_USER_MODEL)),
                ('manager_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='managid', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Progress',
            fields=[
                ('progrss_id', models.AutoField(primary_key=True, serialize=False)),
                ('points', models.FloatField(default=0.0)),
                ('intern_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='intern', to=settings.AUTH_USER_MODEL)),
                ('progress_task_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='progress_task_id', to='core.task')),
            ],
        ),
        migrations.CreateModel(
            name='LoginLogoutLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_key', models.CharField(max_length=100)),
                ('host', models.CharField(max_length=100)),
                ('login_time', models.DateTimeField(blank=True, null=True)),
                ('logout_time', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Blocker_Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField()),
                ('query', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.blocker')),
            ],
        ),
        migrations.AddField(
            model_name='blocker',
            name='blocker_task_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='taskid', to='core.task'),
        ),
        migrations.AddField(
            model_name='blocker',
            name='intern_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='internid', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='blocker',
            name='manager_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to', to=settings.AUTH_USER_MODEL),
        ),
    ]
