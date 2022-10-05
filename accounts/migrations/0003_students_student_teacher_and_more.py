# Generated by Django 4.0.4 on 2022-05-01 09:43

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_customuser_phone_remove_customuser_phone_no'),
    ]

    operations = [
        migrations.CreateModel(
            name='students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('accounts.customuser',),
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('accounts.customuser',),
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.RenameField(
            model_name='customuser',
            old_name='is_serviceBusiness',
            new_name='is_businessEducator',
        ),
        migrations.RenameField(
            model_name='customuser',
            old_name='is_serviceProvider',
            new_name='is_educator',
        ),
    ]
