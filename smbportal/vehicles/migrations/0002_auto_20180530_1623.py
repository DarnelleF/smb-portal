# Generated by Django 2.0.5 on 2018-05-30 16:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bike',
            name='other_details',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='bike',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bikes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='bikepossessionhistory',
            name='bike',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='possession_history', to='vehicles.Bike'),
        ),
    ]