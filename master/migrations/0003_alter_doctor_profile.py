# Generated by Django 5.0 on 2024-07-04 07:38

import master.utils.genrate_unique_id
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0002_doctor_reporttype_patient_paid_installment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='profile',
            field=models.ImageField(default='default_images\\doctor-profile.png', null=True, upload_to=master.utils.genrate_unique_id.custom_filename),
        ),
    ]
