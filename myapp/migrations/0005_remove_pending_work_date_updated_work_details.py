# Generated by Django 5.0.4 on 2024-05-02 11:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_pending_work_date_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pending_work',
            name='date_updated',
        ),
        migrations.CreateModel(
            name='work_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(max_length=100)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('sno_com', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.pending_work')),
            ],
        ),
    ]
