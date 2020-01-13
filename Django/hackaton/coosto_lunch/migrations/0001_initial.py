# Generated by Django 3.0 on 2019-12-13 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Overview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('ADMIN', 'Admin'), ('USER', 'User')], default='USER', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Special',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('overviews', models.ManyToManyField(blank=True, to='coosto_lunch.Overview')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=60)),
                ('role', models.OneToOneField(default='USER', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='coosto_lunch.Role')),
                ('overviews', models.ManyToManyField(blank=True, to='coosto_lunch.Overview')),
            ],
        ),
    ]
