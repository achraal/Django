# Generated by Django 5.1.7 on 2025-04-05 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('missions', '0004_association'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Association',
        ),
        migrations.AddField(
            model_name='mission',
            name='disponibilites_requises',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='mission',
            name='competences_requises',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
