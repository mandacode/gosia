# Generated by Django 4.2.7 on 2023-11-30 20:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('scratchpads', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='scratchpadrecord',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_scratchpad_records', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='scratchpadrecord',
            name='employees',
            field=models.ManyToManyField(related_name='employee_scratchpad_records', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='scratchpad',
            name='records',
            field=models.ManyToManyField(to='scratchpads.scratchpadrecord'),
        ),
    ]
