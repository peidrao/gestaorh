# Generated by Django 3.2.9 on 2021-11-25 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentos', '0003_documento_documento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='documento',
            field=models.FileField(upload_to='arquivos/documentos/'),
        ),
    ]
