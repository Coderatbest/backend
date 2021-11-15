# Generated by Django 3.2.9 on 2021-11-15 01:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentariesModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_activate', models.BooleanField(default=True)),
                ('date_created', models.DateField(auto_now_add=True, help_text='Date time on which the obejec was last created.', verbose_name='created at')),
                ('date_modified', models.DateField(help_text='Date time on which the obejec was last modified.', null=True, verbose_name='modified at')),
                ('body', models.TextField(max_length=70)),
                ('user_created', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='commentaries_commentariesmodels_user_created_name', related_query_name='commentaries_commentariesmodels_user_created_query', to=settings.AUTH_USER_MODEL)),
                ('user_modified', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='commentaries_commentariesmodels_user_modified_name', related_query_name='commentaries_commentariesmodels_user_modified_query', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['date_created', 'date_modified'],
                'get_latest_by': 'date_created',
                'abstract': False,
            },
        ),
    ]
