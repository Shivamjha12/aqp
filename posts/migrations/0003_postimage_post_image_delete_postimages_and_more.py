# Generated by Django 4.0.4 on 2022-09-30 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_rename_images_postimages'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(upload_to='post_images/')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.DeleteModel(
            name='PostImages',
        ),
        migrations.AddField(
            model_name='postimage',
            name='post',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='posts.post'),
        ),
    ]
