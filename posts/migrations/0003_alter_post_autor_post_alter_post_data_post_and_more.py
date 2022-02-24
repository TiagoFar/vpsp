# Generated by Django 4.0.2 on 2022-02-18 20:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0002_alter_post_categoria_post_alter_post_conteudo_post_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='autor_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Autor'),
        ),
        migrations.AlterField(
            model_name='post',
            name='data_post',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='post',
            name='titulo_post',
            field=models.CharField(max_length=255, verbose_name='Titulo'),
        ),
    ]