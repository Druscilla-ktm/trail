# Generated by Django 5.1.5 on 2025-01-16 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_created=True, auto_now_add=True)),
                ('title', models.CharField(max_length=200)),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]
