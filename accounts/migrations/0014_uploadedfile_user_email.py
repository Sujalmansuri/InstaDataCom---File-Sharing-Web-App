# Generated by Django 5.1.6 on 2025-05-10 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_remove_uploadedfile_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadedfile',
            name='user_email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]
