# Generated by Django 4.2.1 on 2023-05-12 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('days', '0002_day'),
        ('habits','0001_create_model_habit')
    ]

    operations = [
        migrations.CreateModel(
            name='DayHabit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed', models.BooleanField(default=False)),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='days.day')),
                ('habit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='habits.habit')),
            ],
        ),
        migrations.AddField(
            model_name='day',
            name='habits',
            field=models.ManyToManyField(through='days.DayHabit', to='habits.habit'),
        ),
    ]
