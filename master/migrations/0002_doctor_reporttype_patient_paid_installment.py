# Generated by Django 5.0 on 2024-01-19 11:37

import django.db.models.deletion
import django.utils.timezone
import master.utils.genrate_unique_id
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('profile', models.ImageField(default='default_images\\doctor-profile.png', upload_to=master.utils.genrate_unique_id.custom_filename)),
                ('name', models.CharField(max_length=255)),
                ('degree', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=255)),
                ('total_patient', models.IntegerField(default=0)),
                ('summary', models.TextField()),
                ('address', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ReportType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('report_charge', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('mobile', models.CharField(max_length=255)),
                ('total_amount', models.FloatField(blank=True)),
                ('paid_amount', models.FloatField(default=0)),
                ('remaining_amount', models.FloatField(blank=True)),
                ('payment_status', models.CharField(default='Pending', max_length=255)),
                ('address', models.TextField()),
                ('doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.doctor')),
                ('report_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.reporttype')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='paid_installment',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('payment_id', models.CharField(blank=True, max_length=255, primary_key=True, serialize=False)),
                ('paid_date', models.DateField(default=django.utils.timezone.now)),
                ('paid_payment', models.FloatField()),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.patient')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
