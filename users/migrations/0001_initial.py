# Generated by Django 4.1.4 on 2022-12-24 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('lat', models.DecimalField(decimal_places=6, max_digits=10, null=True)),
                ('lng', models.DecimalField(decimal_places=6, max_digits=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200, null=True)),
                ('last_name', models.CharField(max_length=200, null=True)),
                ('username', models.CharField(max_length=200, unique=True)),
                ('password', models.CharField(max_length=200)),
                ('role', models.CharField(choices=[('MB', 'member'), ('MD', 'moderator'), ('AD', 'admin')], max_length=2)),
                ('age', models.PositiveSmallIntegerField()),
                ('locations', models.ManyToManyField(to='users.location')),
            ],
        ),
    ]
