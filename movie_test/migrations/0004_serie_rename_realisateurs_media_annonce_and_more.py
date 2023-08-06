# Generated by Django 4.1.7 on 2023-08-06 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_test', '0003_media_acteurs_media_realisateurs'),
    ]

    operations = [
        migrations.CreateModel(
            name='Serie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('year', models.IntegerField()),
                ('genre', models.CharField(max_length=255)),
                ('image_name', models.CharField(max_length=255, null=True)),
                ('acteurs', models.CharField(max_length=255, null=True)),
                ('realisateur', models.CharField(max_length=255, null=True)),
                ('description', models.TextField(null=True)),
                ('annonce', models.CharField(max_length=255, null=True)),
                ('saison', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='media',
            old_name='realisateurs',
            new_name='annonce',
        ),
        migrations.AddField(
            model_name='media',
            name='realisateur',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
