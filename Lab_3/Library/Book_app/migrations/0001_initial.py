# Generated by Django 2.2.12 on 2023-02-03 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('year', models.IntegerField()),
                ('author', models.TextField()),
                ('title', models.TextField()),
                ('genre', models.CharField(default='fantasy', max_length=30)),
                ('inventory_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Borrow',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('due_date', models.DateTimeField()),
                ('is_returned', models.BooleanField(default=False)),
                ('books', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Book_app.Book')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Book_app.Customer')),
            ],
        ),
    ]
