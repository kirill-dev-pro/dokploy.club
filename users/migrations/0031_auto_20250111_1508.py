# Generated by Django 3.2.13 on 2025-01-11 15:08

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0030_auto_20240729_1343'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='geolocation',
            field=models.JSONField(null=True),
        ),
        migrations.RunSQL(
            sql="""
                update users
                set geolocation = (select jsonb_build_object('latitude', latitude, 'longitude', longitude) from geo where geo.id = users.geo_id)
                where users.geo_id is not null;
            """,
            reverse_sql="""
                update users
                set geo_id = (select id from geo where geo.latitude = users.geolocation->>'latitude' and geo.longitude = users.geolocation->>'longitude' limit 1)
                where users.geolocation is not null;
            """
        ),
        migrations.RemoveField(
            model_name='user',
            name='geo',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='geolocation',
            new_name='geo',
        ),
    ]
