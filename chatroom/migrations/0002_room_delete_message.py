# Generated by Django 4.2.3 on 2023-08-23 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatroom', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ROOM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('topic', models.CharField(max_length=40)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Message',
        ),
    ]
