# Generated by Django 3.2.9 on 2021-11-25 00:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('documentos', '0004_alter_documento_documento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='funcionario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='funcionario_doc', to=settings.AUTH_USER_MODEL),
        ),
    ]
