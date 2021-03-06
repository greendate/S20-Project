# Generated by Django 2.2.11 on 2020-03-26 21:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('desctiption', models.TextField()),
                ('image_url', models.CharField(default='https://i.imgur.com/FChk3bD.jpg', max_length=500)),
                ('grade', models.DecimalField(decimal_places=1, default=0.0, max_digits=2)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=50)),
                ('text', models.TextField()),
                ('grade', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=1)),
                ('club_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scqf.Club')),
            ],
        ),
    ]
