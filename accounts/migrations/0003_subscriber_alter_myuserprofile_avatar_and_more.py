# Generated by Django 4.0.1 on 2022-07-22 09:50

import accounts.utils
import accounts.validators
from django.db import migrations, models
import imagekit.models.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_payment_reference'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='myuserprofile',
            name='avatar',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to=accounts.utils.upload_avatar_directory, validators=[accounts.validators.avatar_validator]),
        ),
        migrations.AlterField(
            model_name='payment',
            name='reference',
            field=models.UUIDField(default=uuid.UUID('92d992d9-ad9c-487f-b127-e3642000e6a6')),
        ),
    ]
