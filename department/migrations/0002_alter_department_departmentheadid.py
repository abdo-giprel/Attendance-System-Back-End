# Generated by Django 4.0 on 2021-12-18 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0010_alter_user_managers'),
        ('department', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='departmentHeadID',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='department', to='authentication.user'),
        ),
    ]
