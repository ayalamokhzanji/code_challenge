# Generated by Django 3.0 on 2022-11-13 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('codestar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=30)),
                ('education', models.CharField(max_length=30)),
                ('level', models.CharField(max_length=10)),
                ('prize', models.CharField(max_length=10)),
            ],
        ),
    ]