# Generated by Django 5.0.1 on 2024-02-13 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('side', models.CharField(max_length=5)),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
