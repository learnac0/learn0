# Generated by Django 4.0.1 on 2022-02-02 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_author_delete_userdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='userdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Author',
        ),
    ]
