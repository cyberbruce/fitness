# Generated by Django 4.0.3 on 2022-03-22 21:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_weight_unique_weight_by_day_for_user_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weight',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='weight', to='dashboard.profile'),
        ),
    ]
