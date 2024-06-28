# mytodo/views.py
from django.shortcuts import render, redirect
from django.views import View
from .forms import TaskForm
from .models import models


# Create your views here.
class IndexView(View):
    def get(self, request):
        # todoリストを取得

        # テンプレートをレンダリング
        return render(request, "mytodo/index.html")

class AddView(View):
    def get(self,request):
        form = TaskForm()
        
        #テンプレートのレンダリングの処理
        return render(request,"mytodo/add.html",{'form':'form'})
    
    def post(self,request,*args, **kwargs):
        #登録の処理
        form = TaskForm(request.POST)
        #入力データに誤りがないかチェック
        is_valid = form.is_valid()
        
        #データが正常であれば
        if is_valid:
            #モデルに登録
            form.save()
            return redirect('/')
        
        #データが正常じゃない
        return render(request,'mytodo/add.html',{'form':form})
class Update_task_complete(View):
    def post(self, request, *args, **kwargs):
        task_id = request.POST.get('task_id')
        
        task = task.objects.get(id=task_id)
        task.complete = not task.complete
        task.save()
        
        return redirect('/')
        


# ビュークラスをインスタンス化
index = IndexView.as_view()
add = AddView.as_view()
update_task_complete = Update_task_complete.as_view()