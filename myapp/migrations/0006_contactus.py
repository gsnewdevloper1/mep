# Generated by Django 5.0.4 on 2024-05-05 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_remove_pending_work_date_updated_work_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.IntegerField()),
                ('message', models.CharField(max_length=100)),
            ],
        ),
    ]
