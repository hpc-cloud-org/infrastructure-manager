# Generated by Django 4.2.1 on 2023-07-28 08:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("clusters", "0005_clusterconfiguration_nodes_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="clusterconfiguration",
            name="entrypoint_ip",
            field=models.GenericIPAddressField(null=True),
        ),
    ]