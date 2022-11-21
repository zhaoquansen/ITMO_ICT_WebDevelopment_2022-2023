# Generated by Django 4.1.3 on 2022-11-02 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_delete_test_carowner_home_address_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=15)),
                ('brand', models.CharField(max_length=20)),
                ('model', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pass_number', models.CharField(max_length=10, null=True)),
                ('address', models.CharField(max_length=30, null=True)),
                ('nat', models.CharField(max_length=10, null=True)),
                ('last_name', models.CharField(max_length=30)),
                ('first_name', models.CharField(max_length=30)),
                ('birth_date', models.DateTimeField(null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='possession',
            old_name='date_end',
            new_name='end',
        ),
        migrations.RenameField(
            model_name='possession',
            old_name='date_start',
            new_name='start',
        ),
        migrations.RemoveField(
            model_name='possession',
            name='id_vehicle',
        ),
        migrations.DeleteModel(
            name='Vehicle',
        ),
        migrations.AddField(
            model_name='possession',
            name='id_car',
            field=models.ManyToManyField(to='first_app.car'),
        ),
        migrations.AlterField(
            model_name='driverlicense',
            name='id_owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_app.owner'),
        ),
        migrations.AlterField(
            model_name='possession',
            name='id_owner',
            field=models.ManyToManyField(to='first_app.owner'),
        ),
        migrations.DeleteModel(
            name='CarOwner',
        ),
    ]
