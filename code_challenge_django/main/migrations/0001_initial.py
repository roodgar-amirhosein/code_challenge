# Generated by Django 5.0.3 on 2024-03-15 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(choices=[('user1', 'user1'), ('user2', 'user2')], max_length=10)),
                ('stock', models.CharField(choices=[('stock1', 'stock1'), ('stock2', 'stock2'), ('stock3', 'stock3')], max_length=10)),
                ('status', models.CharField(choices=[('Accepted', 'Accepted'), ('Denied', 'Denied')], max_length=15)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('price', models.PositiveIntegerField()),
                ('quantity', models.PositiveIntegerField()),
            ],
        ),
    ]
