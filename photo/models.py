from django.db import models

from accounts.models import CustomUser

class Category(models.Model):
    #カテゴリ名のフィールド
    title = models.CharField(
        verbose_name= 'カテゴリ',# フィールドのタイトル
        max_length=20
        )
    
    def __str__(self):
        '''オブジェクトを文字列に変換して返す
        
        Returns(str):カテゴリ名
        '''
        return self.title
    
class PhotoPost(models.Model):
    '''モデルクラス
    '''
    #CustomUserモデル(のuser_id)とPhotoPostモデルを
    #1対多の関係で結びつける
    #CustomUserが親でPhotoPostが子の関係となる
    user = models.ForeignKey(
        CustomUser,
        #フィールドのタイトル
        verbose_name='ユーザー',
        #カテゴリに関連つけられた投稿データが存在する場合
        #そのカテゴリを削除できないようにする
        on_delete=models.CASCADE
        )
    #Categoryモデル（のtitle）とPhotoPostモデルを
    #一対多の関係で結びつける
    #Categoryが親でPhotoPostが子の関係となる
    category = models.ForeignKey(
        Category,
        #フィールドのタイトル
        verbose_name='カテゴリ',
        #カテゴリに関連つけられた投稿データが存在する場合は
        #そのカテゴリを削除できないようにする
        on_delete=models.PROTECT
        )
    #タイトル用のフィールド
    title = models.CharField(
        verbose_name='タイトル',
        max_length=200,
        )
    #タイトル用のフィールド
    comment = models.TextField(
        verbose_name='コメント',
        )
    #イメージのフィールド１
    image1 = models.ImageField(
        verbose_name='イメージ１',
        upload_to='photos',
        #photosフォルダーは自動生成される
        
        )
    #イメージのフィールド２
    image2 = models.ImageField(
        # フィールドのタイトル
        verbose_name='イメージ２',
        # MEDIA_ROOT以下のphotosにファイルを保存
        upload_to='photos',
        # フィールド値の設定は必須でない
        blank=True,
        # データベースにnullが保存されることを許容
        null=True,
        )
    #投稿日時のフィールド
    posted_at = models.DateTimeField(
        # フィールドのタイトル
        verbose_name='投稿日時',
        # 日時を自動追加
        auto_now_add=True,
        )
    
    def __str__(self):
        '''オブジェクトを文字列に変換して返す
        
           Returns(str):投稿記事のタイトル
        '''
        return self.title
        
    

























