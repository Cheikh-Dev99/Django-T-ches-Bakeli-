# Generated by Django 5.1.1 on 2024-11-07 01:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mangalib', '0007_alter_livre_titre'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='auteur',
            options={'verbose_name': 'Auteur', 'verbose_name_plural': 'Auteurs'},
        ),
        migrations.AlterModelOptions(
            name='livre',
            options={'verbose_name': 'Livre', 'verbose_name_plural': 'Livres'},
        ),
    ]
