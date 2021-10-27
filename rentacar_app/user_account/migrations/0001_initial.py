from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('first_name', models.CharField(blank=True, max_length=60)),
                ('last_name', models.CharField(blank=True, max_length=60)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('hide_email', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ClientProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='user_account.account')),
                ('phone_number', models.CharField(blank=True, max_length=20)),
                ('address1', models.CharField(blank=True, max_length=50)),
                ('address2', models.CharField(blank=True, max_length=30)),
                ('postcode', models.CharField(blank=True, max_length=10)),
                ('state', models.CharField(blank=True, max_length=30)),
                ('country', models.CharField(blank=True, max_length=20)),
                ('state_region', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='user_account.account')),
                ('payment', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
