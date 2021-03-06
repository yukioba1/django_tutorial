# Generated by Django 3.0.2 on 2021-07-18 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='ユーザー名')),
                ('profile_image', models.CharField(blank=True, max_length=255, null=True, verbose_name='プロファイル画像')),
                ('email', models.CharField(max_length=255, unique=True, verbose_name='メールアドレス')),
                ('password', models.CharField(max_length=255, verbose_name='パスワード')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='登録日時')),
                ('updated_at', models.DateTimeField(blank=True, null=True, verbose_name='更新日時')),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
