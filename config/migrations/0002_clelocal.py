# Generated by Django 3.0.1 on 2020-05-05 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CleLocal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cle_local', models.CharField(max_length=255)),
            ],
        ),
    ]
