# Generated by Django 2.2.2 on 2023-10-23 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20231020_1911'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentinfo',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='email',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='mobileno1',
            field=models.IntegerField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='mobileno2',
            field=models.IntegerField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='town',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
