# Generated by Django 5.0.4 on 2024-04-15 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=150)),
                ('choice1', models.CharField(max_length=50)),
                ('choice2', models.CharField(max_length=50)),
                ('choice3', models.CharField(max_length=50)),
                ('choice4', models.CharField(max_length=50)),
                ('answer', models.CharField(max_length=50)),
            ],
        ),
    ]