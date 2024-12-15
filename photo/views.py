from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from django.views.generic import CreateView,DetailView,DeleteView
from django.urls import reverse_lazy
from .forms import PhotoPostForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import PhotoPost


class IndexView(ListView):
    '''トップページのビュー
    '''
    
    #index.htmlをレンダリングする
    template_name = 'index.html'
    #モデルPhotoPostのオブジェクトにorder_byを適用して
    #投稿日時の降順で並べ替える
    queryset = PhotoPost.objects.order_by('-posted_at')#all()はListViewが適時行ってくれる
    #1ページに表示するレコードの件数
    paginate_by = 9

#デコレーターによりCreatePhotoViewクラスへのアクセスはログインユーザのみに設定される
#ログイン状態でないユーザはsetting.pyのLOGIN_URLにリダイレクトされる
@method_decorator(login_required,name='dispatch')
class CreatePhotoView(CreateView):
    '''
    写真投稿ページのビュー
    
    PhotoPostFormで定義されているmodelとfieldsを連携して
    データベースに投稿データを登録する
    
    Attributes:
        form_class:modelとfieldsが登録されたフォームクラス
        template_name:レンダリングするテンプレート
        success_url:データベースへの登録が完了した後のレンダリング先
    '''
    # form_classにforms.pyのPostPhotoFormを登録
    form_class = PhotoPostForm
    # templateにpost_photo.htmlを登録
    template_name ='post_photo.html'
    # success_urlにreverse_lazyでphotoアプリのpost_doneを設定
    success_url = reverse_lazy('photo:post_done')
    
    def form_valid(self,form):
        '''
        CreateViewクラスのform_validメソッドをoverride
        
        フォームのバリデーションを突破したときに呼ばれるメソッド
        フォームデータの登録を行う
        
        parameters:
            form(django.forms.Form):
                form_classに格納されているPhotoPostFormオブジェクト
        Return:
            HttpResposeRedirectオブジェクト:
                スーパークラスのform_validに戻り値を与えることで
                success_urlで設定されているURLにリダイレクトされる
        '''
        # 
        postdata = form.save(commit=False)
        #form.save →　form-input dataを使用してモデルインスタンスを生成or更新する
        #commit　→　データベースに反映するかを判断する 
        #-→　postdataはフォームから生成されたデータベースに反映されないモデルインスタンス
        
        # self.requetでuser情報を取得してpostdata.userフィールドに格納している
        postdata.user = self.request.user
        # 投稿データをデータベースに保存 save the posted data to the database
        postdata.save()
        #戻り値はスーパークラスのform_valid()の戻り値(HttpResponseRedirect) 
        #親クラスをreturnする理由は親クラスの処理を継承するため
        return super().form_valid(form)
    
class PostSuccessView(TemplateView):
    '''
    投稿完了のページビュー
    
    Attributes:
        template_name:レンダリングするテンプレート
    '''
    #レンダリングするページを指定
    template_name = 'post_success.html'
    
class CategoryView(ListView):
    '''カテゴリーページのビュー
    
    '''
    template_name = 'index.html'
    paginate_by = 9
    
    def get_queryset(self):
        '''クエリを実行する
        
        self.kwargsの取得が必要なため、クラス変数querysetではなく
        get_queryset()のオーバーライドによりクエリを実行する
        
        Returns:
            クエリによって取得されたレコード
        '''
        
        #self.kwargsでキーワードの辞書を取得して
        #categorykeyの値(categoryテーブルのid)を取得する
        category_id = self.kwargs['category']
        #filter(フィールド名=id)で絞り込む
        categories = PhotoPost.objects.filter(
            category=category_id).order_by('-posted_at')
        #クエリによって取得されたレコードを返す
        return categories
    
class UserView(ListView):
    '''ユーザの投稿一覧を表示する
    '''
    template_name = 'index.html'
    pagenate_by = 9
    
    def get_queryset(self):
        user_id = self.kwargs['user']
        user_list = PhotoPost.objects.filter(
            user=user_id).order_by('-posted_at')
        return user_list
    
class DetailView(DetailView):
    '''詳細ページのビュー
    '''
    template_name = 'detail.html'
    model = PhotoPost
    #DetailViewは継承することでquerysetを自動で作成してくれるためこのクラスには定義する必要はない
    
class MypageView(ListView):
    template_name = 'mypage.html'
    pagenate_by = 9
    def get_queryset(self):
        queryset = PhotoPost.objects.filter(
            user = self.request.user).order_by('-posted_at')
        return queryset
    
class PhotoDeleteView(DeleteView):
    model = PhotoPost
    template_name = 'photo_delete.html'
    success_url = reverse_lazy('photo:mypage')
    
    def delete(self,request,*args,**kwargs):
        response = super().delete(request,*args,**kwargs)
        return response
'''
スーパークラスのdeleteメソッド
def delete(self,request,*args,**kwargs):
    self.object= self.get_object()
    success_url= self.get_success_url()
    self.object.delete()
    return HttpResponseRedirect(success_url)
    
    def delete(self,request,*args,**kwargs):
        レコードの削除を行う
        Parameters:
            self:PhotoDeleteViewオブジェクト
            request:WSGIrequest(HttpRequest)オブジェクト
            args:引数として渡される辞書
            kwargs:キーワード付きの辞書
                    {pk: 21}のようにレコードのidが渡される
        
        Returns:
            HttpResponseRedirect(success_url)を返して
            success_urlをリダイレクト
        
        return super().delete(request,*args,**kwargs)
'''






        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
