# Generated by Django 2.0.5 on 2018-07-09 16:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20180709_1914'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='approved_comments',
            new_name='approved_comment',
        ),
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
    ]
