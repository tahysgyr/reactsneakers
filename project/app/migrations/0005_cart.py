<<<<<<< HEAD
# Generated by Django 4.1.6 on 2023-08-24 17:22
=======
# Generated by Django 4.2.4 on 2023-08-11 18:33
>>>>>>> 22fde60a6e69883344a0e6115f03b0ccac886a50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0004_products_description_products_specifications_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quanity', models.PositiveIntegerField(default=1)),
                ('price_sale', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.products')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Корзина',
                'ordering': ['-id'],
            },
        ),
    ]
