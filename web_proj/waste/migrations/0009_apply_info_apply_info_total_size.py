# Generated by Django 2.1 on 2020-06-04 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waste', '0008_auto_20200604_1724'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply_info',
            name='apply_info_total_size',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
    ]