# Generated by Django 4.2.4 on 2024-01-19 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0022_galry_image'),
        ('shop', '0007_client_guest_email_client_guest_name_order_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('Client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.client')),
                ('Item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.item')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='ratings',
            field=models.ManyToManyField(blank=True, related_name='items', to='shop.rating'),
        ),
    ]
