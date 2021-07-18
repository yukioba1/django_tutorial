from django.db import models


class User(models.Model):
	# ユーザーモデル
    class Meta:
    	# テーブル名定義
    	db_table = 'users'

    # テーブルフィールド定義
    name = models.CharField(verbose_name='ユーザー名', max_length=255)
    profile_image = models.CharField(
        verbose_name='プロファイル画像', max_length=255, null=True, blank=True)
    email = models.CharField(verbose_name='メールアドレス',
                             max_length=255, unique=True)
    password = models.CharField(verbose_name='パスワード', max_length=255)
    created_at = models.DateTimeField(verbose_name='登録日時', auto_now_add=True)
    updated_at = models.DateTimeField(
        verbose_name='更新日時', null=True, blank=True)
