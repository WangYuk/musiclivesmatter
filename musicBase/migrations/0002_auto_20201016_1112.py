# Generated by Django 2.1.7 on 2020-10-16 03:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('musicBase', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_id', models.IntegerField()),
                ('album_name', models.CharField(max_length=50)),
                ('album_data', models.DateTimeField()),
                ('album_singer_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Singer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('singer_id', models.IntegerField()),
                ('singer_name', models.CharField(max_length=20)),
                ('singer_gender', models.CharField(max_length=10)),
                ('singer_msg', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_id', models.IntegerField()),
                ('song_name', models.CharField(max_length=50)),
                ('song_singer_id', models.IntegerField()),
                ('song_album_id', models.IntegerField()),
                ('song_produce', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='SongComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_id', models.IntegerField()),
                ('comment_song_id', models.IntegerField()),
                ('comment_msg', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SongLikes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like_id', models.IntegerField()),
                ('like_song_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(null=True)),
                ('user_name', models.CharField(max_length=20, null=True)),
                ('password', models.CharField(max_length=20, null=True)),
                ('user_gender', models.CharField(max_length=10, null=True)),
                ('user_com_type', models.CharField(max_length=20, null=True)),
                ('user_com', models.CharField(max_length=30, null=True)),
                ('user_birthday', models.DateTimeField(null=True)),
                ('user_show_message', models.BooleanField(null=True)),
                ('user_show_likes', models.BooleanField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='songlikes',
            name='like_user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='musicBase.User'),
        ),
    ]
