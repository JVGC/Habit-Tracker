# Generated by Django 4.2.1 on 2023-05-12 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0002_day'),
    ]

    operations = [
        migrations.CreateModel(
            name='DayHabit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checked', models.BooleanField(default=False)),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='habits.day')),
                ('habit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='habits.habit')),
            ],
        ),
        migrations.AddField(
            model_name='day',
            name='habits',
            field=models.ManyToManyField(through='habits.DayHabit', to='habits.habit'),
        ),
    ]
