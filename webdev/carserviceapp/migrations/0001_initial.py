# Generated by Django 3.1.6 on 2021-03-27 12:44

import address.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import multiselectfield.db.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('address', '0003_auto_20200830_1851'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=60, unique=True)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('phone_number', models.IntegerField(unique=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_login', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('shop_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('shop_name', models.CharField(max_length=50)),
                ('owner_name', models.CharField(max_length=50)),
                ('shop_email', models.EmailField(max_length=60, unique=True)),
                ('shop_contact', models.IntegerField(unique=True)),
                ('owner_contact', models.IntegerField(unique=True)),
                ('vehicle_servicing_charge', models.IntegerField()),
                ('vehicle_breakdown_Support_charge', models.IntegerField()),
                ('vehicle_parts_Replacement_charge', models.IntegerField()),
                ('vehicle_modification_charge', models.IntegerField()),
                ('body_repair_and_repainting_charge', models.IntegerField()),
                ('shop_image', models.ImageField(upload_to='')),
                ('shop_location', address.models.AddressField(on_delete=django.db.models.deletion.CASCADE, to='address.address')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('booking_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('services_required', multiselectfield.db.fields.MultiSelectField(choices=[(1, 'Vehicle Servicing'), (2, 'Vehicle Breakdown Support'), (3, 'Vehicle Parts Replacement'), (4, 'Vehicle Modification'), (5, 'Body Repair & Repainting')], max_length=9)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('cost', models.IntegerField(default=100)),
                ('customer', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('hired_shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carserviceapp.shop')),
            ],
        ),
    ]
