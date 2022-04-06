# Generated by Django 4.0.3 on 2022-04-06 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_remove_weight_unique_weight_entry_per_date_and_profife_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='weight',
            name='unique_weight_entry_per_date_and_profife',
        ),
        migrations.AddConstraint(
            model_name='weight',
            constraint=models.UniqueConstraint(condition=models.Q(('entry_date__isnull', False)), fields=('profile', 'entry_date'), name='unique_weight_entry_per_date_and_profife'),
        ),
    ]
