# Generated by Django 2.1.7 on 2019-03-17 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='repository',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=150)),
                ('LastCommit', models.DateField()),
                ('LastConsultation', models.DateField(auto_now=True)),
            ],
        ),
    ]
