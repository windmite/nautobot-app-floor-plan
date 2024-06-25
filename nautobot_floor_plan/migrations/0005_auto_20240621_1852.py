# Generated by Django 3.2.21 on 2024-06-21 18:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("dcim", "0049_remove_slugs_and_change_device_primary_ip_fields"),
        ("nautobot_floor_plan", "0004_auto_20240321_1438"),
    ]

    operations = [
        migrations.AddField(
            model_name="floorplantile",
            name="allocation_type",
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name="floorplantile",
            name="on_group_tile",
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name="floorplantile",
            name="rack_group",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="rack_groups",
                to="dcim.rackgroup",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="floorplantile",
            unique_together={("floor_plan", "x_origin", "y_origin", "allocation_type")},
        ),
    ]
