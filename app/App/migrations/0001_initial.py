# Generated by Django 3.2 on 2022-05-04 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('text', models.TextField()),
                ('answer', models.TextField()),
                ('data', models.DateTimeField()),
            ],
        ),
    ]
