# Generated by Django 4.2.3 on 2023-08-15 08:54

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ('consumer', '0003_products_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUUIDModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='products',
            name='create_time',
        ),
        migrations.RemoveField(
            model_name='products',
            name='last_updated',
        ),
    ]
