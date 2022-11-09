# Generated by Django 4.1.2 on 2022-11-09 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('new_app', '0008_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Arrival',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arrivals_img', models.ImageField(upload_to='')),
                ('arrivals_title', models.CharField(max_length=200)),
                ('arrivals_price', models.IntegerField(default=10)),
                ('arrivals_size', models.CharField(max_length=30)),
                ('arrivals_text', models.TextField(max_length=700)),
                ('category', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='new_app.category')),
            ],
        ),
    ]