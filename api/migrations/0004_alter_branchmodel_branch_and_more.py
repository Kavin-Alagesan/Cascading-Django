# Generated by Django 4.0.6 on 2022-07-28 07:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_delete_employeemodel1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branchmodel',
            name='branch',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='empdetailsmodel',
            name='emp_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.employeemodel'),
        ),
        migrations.AlterField(
            model_name='employeemodel',
            name='branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.branchmodel'),
        ),
    ]