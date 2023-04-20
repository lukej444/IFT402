# Generated by Django 4.1.5 on 2023-02-19 23:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('Department_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Department_Name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('Employee_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Last_Name', models.CharField(max_length=16)),
                ('First_Name', models.CharField(max_length=16)),
                ('Street_Address', models.CharField(max_length=75)),
                ('City', models.CharField(max_length=16)),
                ('State', models.CharField(max_length=10)),
                ('Zip_Code', models.IntegerField(default=0)),
                ('Job_Assignment', models.CharField(max_length=25)),
                ('Department_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='training_app.department')),
            ],
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Training_ID', models.IntegerField()),
                ('Percent_Completed', models.IntegerField()),
                ('Completion_Date', models.DateField()),
                ('Due_Date', models.DateField()),
                ('Employee_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='training_app.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Supervisor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Department_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='training_app.department')),
                ('Employee_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='training_app.employee')),
            ],
        ),
    ]