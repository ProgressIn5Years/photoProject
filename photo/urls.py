from django.urls import path
from . import views

app_name = 'photo'

urlpatterns = [
    
    
    path('',views.IndexView.as_view(),
         name= 'index' ),
    
    #写真投稿ページへのアクセスはviewsモジュールのCreatePhotoViewを実行 
    path('post/',views.CreatePhotoView.as_view(),
         name='post'),
    
    #投稿完了ページへのアクセスはviewsモジュールのPostSuccessViewを実行  
    path('post_done',views.PostSuccessView.as_view(),
         name='post_done'),
    
    #カテゴリ一覧ページ
    #photos/<categoryテーブルのid値>とマッチング
    #<int:category>は辞書{category:id値(int)}としてcategoryViewに与えられる
    path('photos/<int:category>/',
         views.CategoryView.as_view(),
         name ='photos_cat'),
    
    #ユーザの投稿一覧ページ
    #photos/<ユーザーテーブルのid値>とマッチング
    #<int:user>は辞書{user:id値(int)}としてUserViewに与えられる
    path('user-list/<int:user>/',
         views.UserView.as_view(),
         name = 'user_list'),
    
    #詳細ページ
    #photo-detail/<photo postテーブルのid値>とマッチング
    #<int:pk>は辞書{pk:id値(int)}としてDetailViewに与えられる
    path('photo-detail/<int:pk>/',
         views.DetailView.as_view(),
         name ='photo_detail'),
    
    #マイページ
    path('mypage/',views.MypageView.as_view(),
         name = 'mypage'),
    
    #投稿写真の削除
    #photo/<photo postsテーブルのid値>/delete/とマッチング
    #<int:pk>は辞書{pk:id値(int)}としてDetailViewに与えられる
    path('photo/<int:pk>/delete/',
         views.PhotoDeleteView.as_view(),
         name ='photo_delete'),
    
    
]





















