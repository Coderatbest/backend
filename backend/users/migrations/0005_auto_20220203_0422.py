# Generated by Django 3.2.8 on 2022-02-03 04:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_profile_biography'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagesProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='users/profile/imgs_extra')),
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='users/profile/', verbose_name='profile picture'),
        ),
        migrations.AddField(
            model_name='profile',
            name='imgs_extra',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.imagesprofile'),
        ),
    ]
