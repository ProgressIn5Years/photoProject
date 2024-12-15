from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    
    path('', include('photo.urls')),
    
    path('',include('accounts.urls')),
    
    #PassWordResetConfirmViewがプロジェクトのurls.pyを参照するのでここに記載
    #↓
    #パスワードリセットページをプロジェクトのurlconfに記述しない場合、errorが発生する
    #nameオプションに設定する名前はそれぞれauth.urlsで定義済みの名前を使用することでビルトインクラスををサブクラスで使用できる
    
    #パスワードリセット申し込みページ
    path('password_reset/',
         auth_views.PasswordResetView.as_view(
             template_name = "password_reset.html"),
         name = 'password_reset'),
    
    #メール送信完了ページ
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name = "password_reset_sent.html"),
         name = 'password_reset_done'),
    
    #パスワードリセットページ
    path('reset/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(
             template_name = "password_reset_form.html"),
         name = 'password_reset_confirm'),
    
    #パスワードリセット完了ページ
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name = "password_reset_done.html"),
         name = 'password_reset_complete'),
]

#urlpatternsにmediaフォルダーのURLパターンを追加する
urlpatterns += static(
    settings.MEDIA_URL,  #MEDIS_URL= '/media/'
    document_root=settings.MEDIA_ROOT  #MEDIA_ROOTにリダイレクト 
    )















