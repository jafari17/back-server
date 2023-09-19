# Generated by Django 4.1.7 on 2023-09-19 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_date', models.DateField()),
                ('type_position', models.CharField(max_length=20)),
                ('currency', models.CharField(max_length=20)),
                ('entry_price', models.DecimalField(decimal_places=5, max_digits=12)),
                ('dollar_value', models.DecimalField(decimal_places=5, max_digits=12)),
                ('coin_value', models.DecimalField(decimal_places=5, max_digits=12)),
                ('notes', models.CharField(default=None, max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
