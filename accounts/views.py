from django.shortcuts import render
from django.views.generic import CreateView,TemplateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    #formクラスで定義したフォームのクラス
    form_class = CustomUserCreationForm
    #レンダリングするテンプレート
    template_name = 'signup.html'
    #サインアップ完了後のリダイレクト先のURLパターン
    success_url = reverse_lazy('accounts:signup_success')
    
    def form_valid(self,form):
        '''
        CreateViewクラスのform_validメソッドをオーバーライド
        
        フォームのバリデーションを通過した際に呼び出される
        フォームデータの登録を行う
        
        parameters:
            form(django.forms.Form):
           form_classに格納されているCustomUserCreationFormオブジェクト
       Return:
           HttpResponseRedirectオブジェクト:
               スーパークラスのform_valid()の戻り値を返すことで、
               success_urlで設定されているURLにリダイレクトさせる
        '''
        #formオブジェクトのフィールドの値をデータベースに保存
        user = form.save()
        self.object = user
        """
        フォームのバリデーションが成功した際に呼び出され、
        フォームデータを保存してリダイレクトする。
        """
        return super().form_valid(form)
    
        
        
class SignUpSuccessView(TemplateView):
    '''サインアップ完了ページのビュー
    '''
    #レンダリングするテンプレート
    template_name = 'signup_success.html'
    