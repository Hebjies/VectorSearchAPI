# Generated by Django 4.2.10 on 2024-02-26 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('docx_file', models.FileField(upload_to='../../documents/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]