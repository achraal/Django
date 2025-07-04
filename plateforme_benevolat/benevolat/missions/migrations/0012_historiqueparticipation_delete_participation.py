# Generated by Django 5.1.7 on 2025-04-06 11:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('missions', '0011_participation'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoriqueParticipation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_participation', models.DateTimeField(auto_now_add=True)),
                ('role', models.CharField(blank=True, max_length=100, null=True)),
                ('mission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='missions.mission')),
                ('utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Participation',
        ),
    ]
