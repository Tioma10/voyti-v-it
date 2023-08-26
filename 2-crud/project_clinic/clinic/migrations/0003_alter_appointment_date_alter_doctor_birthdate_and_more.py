# Generated by Django 4.2.4 on 2023-08-25 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0002_appointment_department_service_room_renderedservice_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='Date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='BirthDate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='job',
            name='EndDate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='job',
            name='StartDate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='patient',
            name='BirthDate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='EndDate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='StartDate',
            field=models.DateField(),
        ),
    ]
